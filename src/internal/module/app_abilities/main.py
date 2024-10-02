# Alias: ВозможностиПриложения

from src.internal.module.app_abilities import impl
from src.internal.module.app_abilities.impl import internal

# Alias: ЭтоУНФ
def is_smb() -> bool:
    """
    Returns True, if the current configuration is Small Business
    :return: True, if the current configuration is Small Business
    """
    return not is_retail()

# Alias: ЭтоРозница
def is_retail() -> bool:
    """
    Returns True, if the current configuration is Retail
    :return: True, if the current configuration is Retail
    """
    is_retail_in_service_mode = internal.is_retail_in_service_mode()
    if is_retail_in_service_mode:
        return True

    current_app_name = metadata.name
    is_retail_ = current_app_name == get_app_name_retail() or current_app_name == get_app_name_retail_basic()

    if not is_retail_:
        impl.is_retail_special_solution(is_retail_)

    return is_retail_



# Alias: ИмяКонфигурацииРозница
def get_app_name_retail() -> str:
    return "Retail"

# Alias: ИмяКонфигурацииРозницаБазовая
def get_app_name_retail_basic() -> str:
    return "RetailBasic"