# Alias: ВидыКонтактнойИнформации
from main import app
from src.base.common.string import str_format
from src.base.contact_info.model.contact_info_view import ContactInfoView
from src.platform.db.query import Query


# Alias: ПроверитьУникальностьИдентификатора
def check_identifier_uniqueness(formula_identifier: str, ref: ContactInfoView, parent: ContactInfoView, decline: bool):
    """
    Checks identifier uniqueness in metadata object boundaries for parent contact information, and also checks
    identifier corresponding to writing rules.

    :param formula_identifier: Identifier for formulas.
    :param ref: Reference to current object.
    :param parent: Reference to current's parent object.
    :param decline: Flag for declining if error is containing.
    """
    if bool(formula_identifier):
        is_identifier_rules = True
        checking_identifier = get_formula_identifier(formula_identifier)
        if not checking_identifier.upper() == formula_identifier.upper():
            is_identifier_rules = False

            error_text = ("Identifier \"%1\" is not corresponding to variable naming rules."
                          "Identifier should not contain spaces and special characters.")
            common.tell_user(str_format(error_text, formula_identifier), field="formula_identifier", decline=decline)

            # TODO: Do it with nstr
            lang_code = common.get_main_lang_code()
            event_name = "Additional request writing (information)"
            error_text = ("Identifier \"%1\" is not corresponding to variable naming rules."
                          "Identifier should not contain spaces and special characters.")
            error_text = str_format(error_text, formula_identifier)
            # TODO: Make custom logger
            app.logger.error(f"[{event_name}]: {error_text}")

        if is_identifier_rules:
            top_parent = parent
            while bool(top_parent):
                value = common.get_object_field_value(top_parent, "parent_id")
                if bool(value):
                    top_parent = ContactInfoView.load(value)
                else:
                    break

            if not is_formula_identifier_unique(formula_identifier, ref, top_parent):
                decline = True

                error_text = "In database already contains contact information view with identifier \"%1\" in group \"%2\". Identifier must be unique."
                error_text = str_format(error_text, formula_identifier, top_parent)
                common.tell_user(error_text, field="formula_identifier")

                # TODO: Do it with nstr
                lang_code = common.get_main_lang_code()
                error_text = "In database already contains contact information view with identifier \"%1\" in group \"%2\". Identifier must be unique."
                error_text = str_format(error_text, formula_identifier)
                event_name = "Additional request writing (information)"
                # TODO: Make custom logger
                app.logger.error(f"[{event_name}]: {error_text}")
    else:
        error_text = "Formula identifier is not filled"
        common.tell_user(str_format(error_text, formula_identifier), field="formula_identifier", decline=decline)

        # TODO: Do it with nstr
        lang_code = common.get_main_lang_code()
        event_name = "Additional request writing (information)"
        error_text = "Formula identifier is not filled"
        # TODO: Make custom logger
        app.logger.error(f"[{event_name}]: {error_text}")


# Alias: УникальныйИдентификаторДляФормул
def get_unique_formula_identifier(view_obj: str, current_obj: ContactInfoView, parent: ContactInfoView) -> str:
    """
    Returns unique identifier for formulas (after uniqueness checking).

    :param view_obj: View, from which identifier will be formed.
    :param current_obj: Reference to current object.
    :param parent: Reference to current's parent object.
    :return: Unique formula identifier.
    """
    identifier = get_formula_identifier(view_obj)
    if len(identifier) == 0:
        # View contains special characters or digits.
        prefix = "Identifier"
        identifier = get_formula_identifier(prefix + view_obj)

    top_parent = parent
    while bool(top_parent):
        value = common.get_object_field_value(top_parent, "parent_id")
        if bool(value):
            top_parent = ContactInfoView.load(value)
        else:
            break

    query = Query()
    query.set_query("""
    SELECT
        contact_info_view.formula_identifier AS formula_identifier
    FROM
        contact_info_view AS contact_info_view
    WHERE
        contact_info_view.formula_identifier = &formula_identifier
        AND contact_info_view.id <> &current_obj_id
        AND contact_info_view IN HIERARCHY OF (&top_level_parent);
        
    SELECT
        contact_info_view.formula_identifier AS formula_identifier
    FROM
        contact_info_view AS contact_info_view
    WHERE
        contact_info_view.formula_identifier ILIKE &formula_identifier_ilike
        AND contact_info_view.id <> &current_obj_id
        AND contact_info_view IN HIERARCHY OF (&top_level_parent);
    """)
    query.put_parameter("current_obj_id", current_obj.id)
    query.put_parameter("top_level_parent", top_parent.id)
    query.put_parameter("formula_identifier", identifier)
    query.put_parameter("formula_identifier_ilike", common.prepare_str_to_search_query(identifier) + "%")

    query.execute_packet()
    query_results = query.get_results()
    uniqueness_by_full_correspondence = query_results[0]
    if len(uniqueness_by_full_correspondence) != 0:
        # If have elements with current identifier.
        used_identifiers = {}
        query_like = query_results[1]
        for q in query_like:
            used_identifiers.update({q['formula_identifier'].upper(): True})

        adding_number = 1
        identifier_without_number = identifier
        while not used_identifiers[identifier.upper()] is None:
            adding_number += 1
            identifier = identifier_without_number + adding_number

    used_identifiers = {}
    return identifier


# Alias: ИдентификаторДляФормулУникален
def is_unique_formula_identifier(checking_identifier, current_obj, parent):
    top_level_parent = parent
    while bool(top_level_parent):
        value = common.get_object_field_value(top_level_parent, 'parent_id')
        if bool(value):
            top_level_parent = ContactInfoView.load(value)
        else:
            break

    query = Query()
    query.set_query("""
    SELECT
        table.id
    FROM
        contact_info_view AS table
    WHERE
        table.id <> &current_ref_obj
        AND table.id IN HIERARCHY OF (&top_level_parent)
        AND table.formula_identifier = &formula_identifier
    LIMIT 1
    """)
    query.put_parameter("formula_identifier", checking_identifier)
    query.put_parameter("current_ref_obj", current_obj.id)
    query.put_parameter("top_level_parent", top_level_parent.id)

    query.execute()
    query_result = query.get_results()

    return len(query_result) == 0


# Alias: ИдентификаторДляФормул
def get_formula_identifier(view_str: str):
    """
    Calculates identifier value from view string corresponding to variable naming rules.
    :param view_str: name, string that needs to get from identifier.
    :return: identifier corresponding to variable naming rules.
    """
    special_chars = get_special_chars()

    identifier = ''
    was_special_char = False

    for i in range(1, len(view_str) + 1):
        char = view_str[i]

        if char in special_chars:
            was_special_char = True
            if char == '_':
                identifier += char
        elif was_special_char or i == 1:
            was_special_char = False
            identifier += char.upper()
        else:
            identifier += char

    return identifier


# Alias: СпецСимволы
def get_special_chars():
    ranges = [
        {'min': 0, 'max': 32},
        {'min': 127, 'max': 191}
    ]

    special_chars = list(" .,+,-,/,*,?,=,<,>,(,)%!@#$%&*""№:;{}[]?()\|/`~'^_")
    for range_ in ranges:
        for symbol_code in range(range_['min'], range_['max'] + 1):
            special_chars.append(chr(symbol_code))

    return special_chars


# Alias: НаименованиеДляФормированияИдентификатора
def get_name_for_creating_identifier(name, views):
    if get_current_lang()['lang_code'] != common.get_main_lang_code():
        filter_ = {
            'lang_code': common.get_main_lang_code()
        }
        found_rows = list(filter(lambda x: all(x[key] == value for key, value in filter_.items()), views))
        if len(found_rows) > 0:
            name = found_rows[0]['name']

    return name