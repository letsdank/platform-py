import configparser
import re

import psycopg2
import psycopg2.sql
from Demos.EvtSubscribe_pull import query_text

class Query:
    def __init__(self, query = ""):
        self.original_query = query
        self.query = query
        self.results = []
        self.params = {}
        self.is_packet = False
        self.load_config()

        self.set_query(query)

    def load_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.db_host = config['DATABASE']['HOST']
        self.db_name = config['DATABASE']['NAME']
        self.db_user = config['DATABASE']['USER']
        self.db_password = config['DATABASE']['PASSWORD']

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.db_host,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
        self.cur = self.conn.cursor()

    def set_query(self, query_text_):
        self.query = _replace_in_hierarchy(query_text_)
        self.is_packet = ';' in self.query.strip()

    def get_query(self):
        return self.original_query
    
    def put_parameter(self, param_name, param_value):
        self.params[param_name] = param_value

    def execute(self):
        if not hasattr(self, 'cur'):
            self.connect()
        query_text = self.query
        for param_name, param_value in self.params.items():
            query_text = query_text.replace(f"&{param_name}", self.escape_string(param_value))
        self.cur.execute(query_text)
        self.results = self.cur.fetchall()

    def execute_packet(self):
        if not hasattr(self, 'cur'):
            self.connect()

        # Split the query into individual SELECT queries based on semicolons
        queries = [q.strip() for q in self.query.split(';') if q.strip()]
        self.results = []

        for query_text in queries:
            for param_name, param_value in self.params.items():
                query_text = query_text.replace(f"&{param_name}", self.escape_string(param_value))
            self.cur.execute(query_text)
            self.results.append(self.cur.fetchall())

    def get_result(self, index):
        if self.results is None:
            return None
        return self.results[index]

    def get_results(self):
        if self.results is None:
            return []

        return self.results

    def close(self):
        if hasattr(self, 'cur'):
            self.cur.close()
        if hasattr(self, 'conn'):
            self.conn.close()

    def escape_string(self, s):
        return psycopg2.sql.Literal(s).as_string(self.conn)

def _replace_in_hierarchy(query):
    hierarchy_pattern = re.compile(r"(\w+)\s+IN\s+HIERARCHY\s+OF\s+\((.*?)\)", re.IGNORECASE)

    def hierarchy_replacement(match):
        table_alias = match.group(1)
        param = match.group(2)

        hierarchy_cte = f"""
        WITH RECURSIVE hierarchy_cte AS (
            SELECT id, parent_id
            FROM {table_alias}
            WHERE id = {param}
            
            UNION ALL
            
            SELECT h.id, h.parent_id
            FROM {table_alias} h
            INNER JOIN hierarchy_cte cte ON h.parent_id = cte.id
        )
        """
        return f"{hierarchy_cte} {table_alias.id} IN (SELECT id FROM hierarchy_cte)"

    new_query = re.sub(hierarchy_pattern, hierarchy_replacement, query_text)

    return new_query