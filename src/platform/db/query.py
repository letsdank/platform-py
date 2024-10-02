import psycopg2
import configparser

import psycopg2.sql

class Query:
    def __init__(self, query = ""):
        self.query = query
        self.results = []
        self.params = {}
        self.load_config()

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

    def set_query(self, query_text):
        self.query = query_text

    def get_query(self):
        return self.query
    
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
