# Alias: УправлениеКонтактнойИнформациейПереопределяемый

from src.base_integration.contact_info.module import smb as smb


# Alias: ПриНачальномЗаполненииЭлементов
def on_first_fill_elements(lang_codes: list[str], elements: list[dict], table_parts: dict):
    smb.on_first_fill_elements(lang_codes, elements, table_parts)
