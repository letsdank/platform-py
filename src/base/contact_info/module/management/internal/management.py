# Alias: УправлениеКонтактнойИнформациейСлужебный
from src.base.common.string import str_format
from src.base.contact_info.model.contact_info_type import ContactInfoType
from src.base.contact_info.model.contact_info_view import ContactInfoView


# Alias: ПроверитьПараметрыВидаКонтактнойИнформации
def check_contact_info_view_fields(contact_info_view: ContactInfoView) -> dict:
    result = {
        'has_errors': False,
        'error_text': "",
    }

    if not bool(contact_info_view.name):
        result['has_errors'] = True
        result['error_text'] = str_format('Not filled required field Name in contact information view "%1".',
                                          contact_info_view.predefined_type_name)
        return result

    if contact_info_view.is_group:
        return result

    if not bool(contact_info_view.type):
        result['has_errors'] = True
        result['error_text'] = str_format('Not filled required field Type in contact information view "%1".',
                                          contact_info_view.name)
        return result

    delimiter = ""
    if contact_info_view.type == ContactInfoType.address:
        if not contact_info_view.only_national_address and (contact_info_view.check_correctness or contact_info_view.hide_irrelevant_addresses):
            result['error_text'] = str_format('Address checking parameters was set incorrectly in contact information view "%1".'
                                              'Address correctness checking is available only for Russian addresses', contact_info_view.name)
            delimiter = "\n"

        if contact_info_view.allow_several_values and contact_info_view.store_edit_history:
            result['error_text'] += delimiter + str_format('Address parameters was set incorrectly in contact information view "%1".'
                                                           'Ability to enter several values is not allowed while enabled storing editing changes history.', contact_info_view.name)

    result['has_errors'] = bool(result['error_text'])
    return result
