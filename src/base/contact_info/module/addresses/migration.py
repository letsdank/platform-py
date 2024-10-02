# Alias: РаботаСАдресами

# Alias: ПриНачальномЗаполненииЭлементов
def on_first_fill_elements(lang_codes: list[str], elements: list[dict], table_parts: dict):
    elements.append({
        'predefined_name': 'Россия',
        'code': '543',
        'name': 'РОССИЯ',
        'full_name': 'Россйиская Федерация',
        'code_alpha2': 'RU',
        'code_alpha3': 'RUS',
        'is_eaeu': True,
        'international_name': 'The Russian Federation',
    })