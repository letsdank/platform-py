# Alias: УправлениеКонтактнойИнформацией
from src.platform.db.query import Query

# Alias: КодСтраныМира
def get_world_country_code(country_code):
    """
    Casts country code to one view - string with length of 3 symbols.
    """
    if type(country_code) == int:
        return f"%03.f" % country_code

    return ("000" + country_code)[-3:]

# Alias: ПользовательскиеСтраныЕАЭС
def get_user_eaeu_countries() -> list:
    """
    Returns a list of EAEU countries that was added by the user.

    :return: see get_eaeu_countries()
    """
    query = Query()
    query.set_query("""
    SELECT
        world_country.id AS id,
        world_country.name AS name,
        world_country.code AS code,
        world_country.full_name AS full_name,
        world_country.code_alpha2 AS code_alpha2,
        world_country.international_name AS international_name,
        world_country.code_alpha3 AS code_alpha3
    FROM
        world_country AS world_country
    WHERE
        world_country.is_eaeu = TRUE
    """)

    query.execute()
    return query.get_results()