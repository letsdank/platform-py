# Alias: КонтактнаяИнформацияУНФ
from src.internal.module.smb import common as common_smb

# Alias: ПриНачальномЗаполненииЭлементов
def on_first_fill_elements(lang_codes: list[str], elements: list[dict], table_parts: dict):
    on_first_fill_elements_counterparty(lang_codes, elements, table_parts)
    on_first_fill_elements_contact_person(lang_codes, elements, table_parts)
    on_first_fill_elements_organization(lang_codes, elements, table_parts)
    on_first_fill_elements_individual(lang_codes, elements, table_parts)
    on_first_fill_elements_structural_unit(lang_codes, elements, table_parts)
    on_first_fill_elements_user(lang_codes, elements, table_parts)
    on_first_fill_elements_envd_activity_type(lang_codes, elements, table_parts)
    on_first_fill_elements_trade_point(lang_codes, elements, table_parts)
    on_first_fill_elements_lead(lang_codes, elements, table_parts)
    on_first_fill_elements_lead_contact(lang_codes, elements, table_parts)
    on_first_fill_elements_order_pickup_point(lang_codes, elements, table_parts)

# Alias: ПриНачальномЗаполненииЭлементовКонтрагенты
def on_first_fill_elements_counterparty(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

# Alias: НеиспользуемаяКонтактнаяИнформация
def get_unused_contact_info() -> list[str]:
    if common_smb.is_retail():
        return get_unused_contact_info_retail()
    elif common_smb.is_smb():
        return get_unused_contact_info_smb()
    else:
        return []

# Alias: НеиспользуемаяКонтактнаяИнформацияРозница
def get_unused_contact_info_retail() -> list[str]:
    return [
        'directory_lead',
        'directory_lead_contact',
        'lead_company_email',
        'lead_company_skype',
        'lead_company_other_information',
        'lead_company_website',
        'lead_company_phone',
        'lead_company_actual_address',
        'lead_contact_email',
        'lead_contact_skype',
        'lead_contact_messenger',
        'lead_contact_social_network',
        'lead_contact_phone',
    ]

# Alias: НеиспользуемаяКонтактнаяИнформацияУНФ
def get_unused_contact_info_smb() -> list[str]:
    return [

    ]