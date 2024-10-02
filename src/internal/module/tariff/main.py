# Alias: ТарификацияУНФ
from src.service_tech.tariff_mgmt import module as tariff_mgmt


# Alias: ИдентификаторУслугиРозница
def get_service_id_retail() -> str:
    """
    Retail service identifier
    :return: str
    """
    return "Retail"

# Alias: ИдентификаторПоставщикаУНФ
def get_vendor_id_smb() -> str:
    """
    SMB vendor identifier
    :return: str
    """
    return "Platform_SMB"

# Alias: ИдентификаторПоставщикаКасса
def get_vendor_id_cash() -> str:
    """
    Cash vendor identifier
    :return: str
    """
    return "Platform_Cash"

# Alias: РозницаВРежимеСервиса
def is_retail_in_service_mode() -> bool:
    """
    Retail in service mode.
    :return: bool
    """
    if not common.is_split_enabled():
        return False

    smb_vendor_id = get_vendor_id_smb()
    retail_service_id = get_service_id_retail()

    registered_service_retail = tariff_mgmt.is_registered_license_unlimited_service(smb_vendor_id, retail_service_id)

    if type(registered_service_retail) is not bool:
        return False

    charged_service_retail = is_service_charged(retail_service_id, smb_vendor_id)
    return registered_service_retail and charged_service_retail

# Alias: УслугаТарифицируется
def is_service_charged(service_id, vendor_id):
    service = tariff_mgmt.get_service_by_service_id_and_vendor_id(service_id, vendor_id, False)

    if service is None:
        return False

    result = common.get_object_field_value(service, "charged")
    return result