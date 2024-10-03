# Alias: УправлениеКонтактнойИнформацией
from src.base.common import string
from src.base.contact_info.model.world_country import WorldCountry
from src.base.contact_info.module.management import internal_world_countries
from src.base.contact_info.module.management.world_country_desc import WorldCountryDescription
from src.platform.db.query import Query

from src.base.contact_info.module.management.internal.impl import management as internal_impl


########################################################
# World countries

# Alias: ДанныеСтраныМира
def get_world_country_data(country_code: (str, int) = None, name: str = None) -> (dict | None):
    """
    Determines country data from country model or by classifier.

    :param country_code: Country code from classifier. If not set, then code searching not performs.
    :param name: Country name. If not set, then name searching not performs.
    :return: Country data or None if country does not exist.
    """
    result = None

    if country_code is None and name is None:
        return result

    search_conditions = []
    classifier_filter = {}

    normalized_code = internal_world_countries.get_world_country_code(country_code)
    if country_code is not None:
        search_conditions.append(f"code = '{normalized_code}'")
        classifier_filter['code'] = normalized_code

    if name is not None:
        tmpl_name = " (name = %1 OR international_name = %1)"
        search_conditions.append(string.str_format(tmpl_name, f"'{name}'"))
        classifier_filter['name'] = name

    search_conditions = " AND ".join(search_conditions)

    result = {
        'id': None,
        'code': '',
        'name': '',
        'full_name': '',
        'international_name': '',
        'code_alpha2': '',
        'code_alpha3': '',
        'is_eaeu': False
    }

    query_text = """SELECT
        id, code, name, full_name,
        international_name, code_alpha2, code_alpha3, is_eaeu
    FROM world_country
    WHERE &search_conditions
    GROUP BY
        name
    LIMIT 1
    """

    query_text = query_text.replace('&search_conditions', search_conditions)
    query = Query(query_text)

    query.execute()
    rows = query.get_results()

    if len(rows) > 0:
        result.update(rows[0])
    else:
        if not internal_impl.is_available_modules_addresses():
            return None

        module_addresses = common.get_module('src.base.contact_info.module.addresses')
        classifier_data = module_addresses.get_classifier_table()
        data_rows = list(
            filter(lambda x: all(x[key] == value for key, value in classifier_filter.items()), classifier_data))
        if len(data_rows) == 0:
            return None
        else:
            result.update(data_rows[0])

    return result


# Alias: ДанныеКлассификатораСтранМираПоКоду
def get_world_country_classifier_data_by_code(code: (str | int), code_type: str = 'country_code') -> (dict | None):
    """
    Determines country data by code.

    :param code: Country code by classifier.
    :param code_type: Variants: 'country_code' (default), 'alpha2' or 'alpha3'.
    :return: Country data or None if country does not exist.
    """
    if not internal_impl.is_available_modules_addresses():
        return None

    result = {
        'code': '',
        'name': '',
        'full_name': '',
        'code_alpha2': '',
        'code_alpha3': '',
        'is_eaeu': False
    }

    module_addresses = common.get_module('src.base.contact_info.module.addresses')
    classifier_data = module_addresses.get_classifier_table()

    if code_type == 'alpha2':
        data_row = next(x for x in classifier_data if x['code_alpha2'] == code)
    elif code_type == 'alpha3':
        data_row = next(x for x in classifier_data if x['code_alpha3'] == code)
    else:
        data_row = next(x for x in classifier_data if x['code'] == internal_world_countries.get_world_country_code(code))

    if data_row is None:
        return None

    result.update(data_row)

    return result


# Alias: ДанныеКлассификатораСтранМираПоНаименованию
def get_world_country_classifier_data_by_name(name: str) -> (dict | None):
    """
    Determines country data by country name.

    :param name: Country name.
    :return: Country data or None if country does not exist in classifier.
    """
    if not internal_impl.is_available_modules_addresses():
        return None

    result = {
        'code': '',
        'name': '',
        'full_name': '',
        'code_alpha2': '',
        'code_alpha3': '',
        'is_eaeu': False
    }

    module_addresses = common.get_module('src.base.contact_info.module.addresses')
    classifier_data = module_addresses.get_classifier_table()

    data_row = next(x for x in classifier_data if x['name'] == name)
    if data_row is None:
        return None

    result.update(data_row)

    return result


# Alias: СтранаМираПоКодуИлиНаименованию
def get_world_country_by_code_or_name(code_or_name: str, fill_data: dict = None) -> (WorldCountry | None):
    """
    Returns world country ID by code or name.
    If element does not exist, then it will be created mainly by fill data.

    :param code_or_name: Country code, code Alpha-2, code Alpha-3 or country name, including international name.
    :param fill_data: Data to fill in case of creating new element.
            Structure case are corresponding to WorldCountry table.
    :return: If found several elements, it will return first found element.
            If not exists and fill data is not set, then returns None.
    """
    query = Query()
    query.set_query("""
    SELECT
        world_country.id AS id
    FROM
        world_country AS world_country
    WHERE
        (world_country.code = &code_or_name
            OR world_country.code_alpha2 = &code_or_name
            OR world_country.code_alpha3 = &code_or_name
            OR world_country.name = &code_or_name
            OR world_country.international_name = &code_or_name
            OR world_country.full_name = &code_or_name)
    """)

    query.put_parameter("code_or_name", code_or_name)
    query.execute()
    result = query.get_results()

    if len(result) > 0:
        return WorldCountry.load(result[0][id])

    if not internal_impl.is_available_modules_addresses():
        return None

    module_addresses = common.get_module('src.base.contact_info.module.addresses')
    classifier_data = module_addresses.get_classifier_table()

    query = Query()
    query.set_query("""
    SELECT INTO classifier_table
        classifier_table.code,
        classifier_table.code_alpha2,
        classifier_table.code_alpha3,
        classifier_table.name,
        classifier_table.full_name,
        classifier_table.international_name,
        classifier_table.is_eaeu,
        classifier_table.is_not_actual
    FROM &classifier_table AS classifier_table;

    SELECT
        world_country.code,
        world_country.code_alpha2,
        world_country.code_alpha3,
        world_country.name,
        world_country.full_name,
        world_country.international_name,
        world_country.is_eaeu,
        world_country.is_not_actual
    FROM classifier_table AS world_country
    WHERE
        (world_country.code = &code_or_name
            OR world_country.code_alpha2 = &code_or_name
            OR world_country.code_alpha3 = &code_or_name
            OR world_country.name = &code_or_name
            OR world_country.international_name = &code_or_name
            OR world_country.full_name = &code_or_name)
    """)

    query.put_parameter("classifier_table", fill_data)
    query.put_parameter("code_or_name", code_or_name)
    query.execute()
    result = query.get_results()

    if len(result) > 0:
        fill_data = WorldCountryDescription()
        fill_data.update(common.table_row_to_dict(result))

    if fill_data is None or not 'name' in fill_data or len(fill_data['name']) == 0:
        return None

    sec.set_privileged(True)
    country_obj = WorldCountry(None, None)
    country_obj.update(fill_data)
    country_obj._save()

    return country_obj


# Alias: СтраныУчастникиЕАЭС
def get_eaeu_countries() -> list:
    """
    Returns list of EAEU (Eurasian Economic Union) countries.
    Calling this function can initiate http-query to web-service to work with classifier
    to get actual list of all EAEU countries.

    :return: List of EAEU countries.
    """
    eaeu_countries = internal_world_countries.get_user_eaeu_countries()

    if not internal_impl.is_available_modules_addresses():
        return eaeu_countries

    module_addresses = common.get_module('src.base.contact_info.module.addresses')
    classifier_data = module_addresses.get_classifier_table()

    for country in classifier_data:
        if country['is_eaeu']:
            filter_ = {
                'name': country['name'],
                'code': country['code'],
                'full_name': country['full_name'],
                'code_alpha2': country['code_alpha2'],
                'code_alpha3': country['code_alpha3']
            }

            found_rows = list(filter(lambda x: all(x[key] == value for key, value in filter_.items()), classifier_data))
            if len(found_rows) == 0:
                eaeu_countries.append(filter_)

    return eaeu_countries


# Alias: ЭтоСтранаУчастникЕАЭС
def is_eaeu_country(country: (str | int)) -> bool:
    if type(country) == int:
        query = Query()
        query.set_query("""
        SELECT
            world_country.is_eaeu AS is_eaeu
        FROM
            world_country AS world_country
        WHERE
            world_country.id = &id
        """)

        query.put_parameter("id", country)
        query.execute()

        result = query.get_results()

        if len(result) > 0:
            result_row = result[0]
            return result_row['is_eaeu'] == True
    else:
        found_country = get_world_country_by_code_or_name(country)
        if bool(found_country):
            return found_country['is_eaeu']

    return False