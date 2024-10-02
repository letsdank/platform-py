from main import db
from src.base.common import string
from src.platform.db.query import Query

from src.base.contact_info.module import management
from src.base.contact_info.module.management.internal.impl import management as management_internal_impl

# PREDEFINED
WORLD_COUNTRY_RUSSIA = 1

class WorldCountry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), unique=True)
    name = db.Column(db.String(60), unique=True)
    deleted = db.Column(db.Boolean, default=False)
    predefined = db.Column(db.Boolean, default=False)
    predefined_name = db.Column(db.String(60))

    full_name = db.Column(db.String(100))
    code_alpha2 = db.Column(db.String(2))
    code_alpha3 = db.Column(db.String(3))
    is_eaeu = db.Column(db.Boolean, default=False)
    international_name = db.Column(db.String(100))

    def __init__(self, code, name, deleted=False, predefined=False, predefined_name=None):
        self.code = code
        self.name = name
        self.deleted = deleted
        self.predefined = predefined
        self.predefined_name = predefined_name

    @staticmethod
    def load(id_):
        return WorldCountry.query.get(id_)

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<WorldCountry %r>' % self.name

    # Alias: ПроверитьУникальностьЭлементов
    def check_element_uniqueness(self) -> list[dict[str, str]]:
        """
        Controls element uniqueness in the database.
        In case of a duplicate code, returns its list.
        :return: If in the program duplicates was found, then contains existing elements description.
        """
        result = []

        # Skip non-numeric codes
        if self.code == "0" or self.code == "00" or self.code == "000":
            search_code = "000"
        else:
            search_code = "%03d" % int(self.code)

        query = Query("""
        SELECT code        AS code,
               name        AS name,
               full_name   AS full_name,
               code_alpha2 AS code_alpha2,
               code_alpha3 AS code_alpha3,
               is_eaeu     AS is_eaeu,
               id          AS id
        FROM world_country
        WHERE (code = &code OR name = &name OR code_alpha2 = &code_alpha2 OR code_alpha3 = &code_alpha3 or
               full_name = &full_name)
          AND id <> &id
        LIMIT 10
        """)

        query.put_parameter("id", self.id)
        query.put_parameter("code", search_code)
        query.put_parameter("name", self.name)
        query.put_parameter("full_name", self.full_name)
        query.put_parameter("code_alpha2", self.code_alpha2)
        query.put_parameter("code_alpha3", self.code_alpha3)

        query.execute()
        query_result = query.get_results()
        if len(query_result) == 0:
            return result

        for row in query_result:
            message = {
                "field_name": "",
                "message": ""
            }

            if row['code'] == self.code:
                message['message'] = string.str_format("Country %2 with code %1 already exists. Change the code or use the existing data.",
                                                       self.code, row['name'])
                message['field_name'] = "code"
            elif row['name'] == self.name:
                message['message'] = string.str_format("Country with name %1 already exists. Change the name or use the existing data.",
                                                       row['name'])
                message['field_name'] = "name"
            elif row['full_name'] == self.full_name:
                message['message'] = string.str_format("Country %2 with full name %1 already exists. Change the full name or use the existing data.",
                                                       self.full_name, row['full_name'])
                message['field_name'] = "full_name"
            elif row['code_alpha2'] == self.code_alpha2:
                message['message'] = string.str_format("Country %2 with code Alpha-2 %1 already exists. Change the code Alpha-2 or use the existing data.",
                                                       self.code_alpha2, row['name'])
                message['field_name'] = "code_alpha2"
            elif row['code_alpha3'] == self.code_alpha3:
                message['message'] = string.str_format("Country %2 with code Alpha-3 %1 already exists. Change the code Alpha-3 or use the existing data.",
                                                       self.code_alpha3, row['name'])
                message['field_name'] = "code_alpha3"

            if bool(message['field_name']):
                result.append(message)

        return result

# Alias: ДанныеСтраныМира
def get_world_country_data(country_code: (str | int) = None, name: str = None) -> (dict | None):
    """
    Determines country data from country model or country classifier.
    It's recommended to use base.contact_info.module.management.get_world_country_data().

    :param country_code: Country code from classifier. If not set, then code searching not performs.
    :param name: Country name. If not set, then name searching not performs.
    :return: Country data or None if country does not exist.
    """
    return management.get_world_country_data(country_code, name)

# Alias: ДанныеКлассификатораСтранМираПоКоду
def get_world_country_classifier_data_by_code(code: (str | int), code_type: str = "country_code") -> (dict | None):
    """
    Determines country data from world country classifier.
    It's recommended to use base.contact_info.module.management.get_world_country_classifier_data_by_code().

    :param code: Country code from classifier.
    :param code_type: Variants: country_code (default), alpha2, alpha3.
    :return: Country data or None if country does not exist.
    """
    return management.get_world_country_classifier_data_by_code(code, code_type)

# Alias: ДанныеКлассификатораСтранМираПоНаименованию
def get_world_country_classifier_data_by_name(name: str) -> (dict | None):
    """
    Determines country data from classifier.
    It's recommended to use base.contact_info.module.management.get_world_country_classifier_data_by_name().

    :param name: Country name.
    :return: Country data or None if country does not exist.
    """
    return management.get_world_country_classifier_data_by_name(name)

# Alias: ПриНачальномЗаполненииЭлементов
def on_first_fill_elements(lang_codes: list[str], elements: list[dict], table_parts: dict):
    if management_internal_impl.is_available_modules_addresses():
        module_addresses = common.get_module('src.base.contact_info.module.addresses')
        module_addresses.on_first_fill_elements(lang_codes, elements, table_parts)
