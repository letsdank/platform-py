# Alias: Тарификация

# General module for Tariff management.
#
# Obtaining/releasing licenses for unique services is performed in two stages:
# 1) First, a request to obtain/release a license is made (e.g., at the start of a transaction),
#    passing a unique operation identifier to the tariff management system.
# 2) Then, the operation is either confirmed or canceled
#    (e.g., before completing the transaction).
#
# Important: The "lifetime" of an incomplete operation in the BTS tariffication system is 15 minutes.
# After this time, incomplete operations are automatically canceled.
#

# Alias: УслугаПоИдентификаторуИИдентификаторуПоставщика
def get_service_by_service_id_and_vendor_id(service_id: str, vendor_id: str, raise_exception: bool=True) -> ServiceAbilities:
    """
    Returns a reference to a service by its ID and the vendor ID.

    :param service_id: the service id.
    :param vendor_id: the vendor id.
    :param raise_exception: flag to raise an exception if the service is not found.
    :return: a reference to the service.
    """
    pass

# Alias: ЗарегистрированаЛицензияБезлимитнойУслуги
def is_registered_license_unlimited_service(vendor_id: str, service_id: str) -> bool:
    """
    Checks if the unlimited license for the specified service is registered for the specified user.

    :param vendor_id: identifier of the service provider.
    :param service_id: identifier of the service.
    :return: True if the license is registered.
    """
    pass

# Alias: ЗарегистрированаЛицензияУникальнойУслуги
def is_registered_license_unique_service(vendor_id: str, service_id: str, license_name: str, license_context: str="") -> bool:
    """
    Checks if the unique license for the specified service is registered.

    :param vendor_id: identifier of the service provider.
    :param service_id: identifier of the service.
    :param license_name: user-readable representation of the license.
    :param license_context: additional context for the license.
    :return: True if the license is registered.
    """
    pass

# Alias: ЗанятьЛицензиюУникальнойУслуги
def acquire_license_unique_service(vendor_id: str, service_id: str, license_name: str, operation_id: str, license_context: str="") -> dict:
    """
    Attempts to acquire a license for a unique service.

    :param vendor_id: identifier of the service provider.
    :param service_id: identifier of the service.
    :param license_name: user-readable license name.
    :param operation_id: unique operation identifier required for confirmation.
    :param license_context: additional context for the license.
    :return: Dictionary with the following keys:
    - "result" (bool): True if the license was successfully acquired.
    - "available_licenses" (int): maximum available licenses for the service (if "-1", then unlimited).
    - "occupied_licenses" (int): number of licenses already in use.
    - "free_licenses" (int): number of available licenses (if "-1", then unlimited).
    """
    pass

# Alias: ОсвободитьЛицензиюУникальнойУслуги
def release_license_unique_service(vendor_id: str, service_id: str, license_name: str, operation_id: str,
                                   data_area_code: int=None, license_context: str="",
                                   delete_license_in_all_areas: bool=False) -> bool:
    """
    Attempts to release a unique service license.

    :param vendor_id: identifier of the service provider.
    :param service_id: identifier of the service.
    :param license_name: user-readable license name.
    :param operation_id: unique operation identifier required for confirmation.
    :param data_area_code: data area code (if called from an undivided session).
    :param license_context: additional context for the license.
    :param delete_license_in_all_areas: flag to delete the license across all data areas.
    :return: True if the license was successfully released.
    """
    pass

# Alias: ЗанятьЛицензииЛимитированнойУслуги
def acquire_license_limited_service(vendor_id: str, service_id: str, license_count: int, data_area_code: int=None) -> dict:
    """
    Attempts to acquire licenses for a limited service.

    :param vendor_id: identifier of the service provider.
    :param service_id: identifier of the service.
    :param license_count: number of licenses requested.
    :param data_area_code: data area code (if called from an undivided session).
    :return: Dictionary with the following keys:
    - "result" (bool): True if the license was successfully acquired.
    - "available_licenses" (int): maximum available licenses for the service.
    - "occupied_licenses" (int): number of licenses already in use.
    - "free_licenses" (int): number of available licenses.
    """
    pass

# Alias: ОсвободитьЛицензииЛимитированнойУслуги
def release_license_limited_service(vendor_id: str, service_id: str, license_count: int, data_area_code: int=None) -> bool:
    """
    Attempts to release licenses for a limited service.

    :param vendor_id: identifier of the service provider.
    :param service_id: identifier of the service.
    :param license_count: number of licenses to release.
    :param data_area_code: data area code (if called from an undivided session).
    :return: True if the licenses were successfully released.
    """
    pass

# Alias: ПодтвердитьОперацию
def confirm_operation(operation_id: str) -> bool:
    """
    Confirms a previously requested license operation (either acquire or release).

    :param operation_id: operation identifier passed when the request was made.
    :return: True if the operation was confirmed.
    """
    pass

# Alias: ОтменитьОперацию
def cancel_operation(operation_id: str) -> bool:
    """
    Cancels a previously requested license operation (either acquire or release).
    :param operation_id: operation identifier passed when the request was made.
    :return: True if the operation was canceled.
    """
    pass

# Alias: КоличествоЛицензийУникальнойУслуги
def get_license_count_unique_service(vendor_id: str, service_id: str) -> dict:
    """
    Attempts to get the number of available licenses for a unique service.
    :param vendor_id: identifier of the service provider.
    :param service_id: identifier of the service.
    :return: Dictionary with the following keys:
    - "available_licenses" (int): maximum available licenses for the service.
    - "occupied_licenses" (int): number of licenses already in use.
    - "free_licenses" (int): number of available licenses.
    """
    pass

# Alias: КоличествоЛицензийЛимитированнойУслуги
def get_license_count_limited_service(vendor_id: str, service_id: str, data_area_code: int=None) -> dict:
    """
    Attempts to get the number of available licenses for a limited service.

    :param vendor_id: identifier of the service provider.
    :param service_id: identifier of the service.
    :param data_area_code: data area code (if called from an undivided session).
    :return: Dictionary with the following keys:
    - "available_licenses" (int): maximum available licenses for the service.
    - "occupied_licenses" (int): number of licenses already in use.
    - "free_licenses" (int): number of available licenses.
    """
    pass

# Alias: ТекущийСеансЗаблокирован
def is_current_session_blocked() -> bool:
    """
    Returns whether the current session is blocked by tariffication.
    :return: True if the session is blocked.
    """
    return False