# Alias: ВозможностиПриложения
from src.internal.module import tariff as smb_tariff

# Alias: ЭтоРозницаВРежимеСервиса
def is_retail_in_service_mode():
    if smb_tariff.is_retail_in_service_mode():
        return True

    if is_retail_in_offline_work_place():
        return True

    return False

# Alias: РозницаВАвтономномРабочемМесте
def is_retail_in_offline_work_place() -> bool:
    """
    Is retail in offline work place
    :return: bool
    """

    # common.is_offline_work_place() performs loop cycle,
    # because it initiates data_exchange_impl.get_exchange_plans() and
    # data_exchange_smb.get_exchange_plans(), which calls common_smb.is_smb().
    if not common.is_subordinate_ddb_node(): # TODO: Distributed Database
        return False

    result = constants.retail_in_offline_work_place.get()
    return result