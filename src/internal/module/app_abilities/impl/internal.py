# Alias: ВозможностиПриложения
from src.internal.module import tariff as smb_tariff

# Alias: ЭтоРозницаВРежимеСервиса
def is_retail_in_service_mode():
    if smb_tariff.is_retail_in_service_mode():
        return True

    if is_retail_in_offline_work_place():
        return True

    return False