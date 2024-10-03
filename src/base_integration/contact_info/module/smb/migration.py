# Alias: КонтактнаяИнформацияУНФ
from src.base.contact_info.model.contact_info_type import ContactInfoType
from src.base.contact_info.model.contact_info_view import CONTACT_INFO_PD
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

    name = 'directory_counterparty'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Контрагенты"'},
                                   lang_codes)
    elements.append(element)

    name = 'counterparty_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'}, lang_codes)
    elements.append(element)

    name = 'counterparty_email'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.email.name,
        'field_additional_ordering': 2,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'check_correctness': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'E-mail'}, lang_codes)
    elements.append(element)

    name = 'counterparty_legal_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 3,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Юр. адрес'}, lang_codes)
    elements.append(element)

    name = 'counterparty_actual_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 4,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Факт. адрес'}, lang_codes)
    elements.append(element)

    name = 'counterparty_delivery_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 5,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Доставка'}, lang_codes)
    elements.append(element)

    name = 'counterparty_skype'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.skype.name,
        'field_additional_ordering': 6,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Skype'}, lang_codes)
    elements.append(element)

    name = 'counterparty_website'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.website.name,
        'field_additional_ordering': 7,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Сайт'}, lang_codes)
    elements.append(element)

    name = 'counterparty_fax'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.fax.name,
        'field_additional_ordering': 8,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Факс'}, lang_codes)
    elements.append(element)

    name = 'counterparty_postal_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 9,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Почтовый адрес'}, lang_codes)
    elements.append(element)

    name = 'counterparty_other_information'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['counterparty']['__id__'],
        'type': ContactInfoType.other.name,
        'field_additional_ordering': 10,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Другое'}, lang_codes)


# Alias: ПриНачальномЗаполненииЭлементовКонтактныеЛица
def on_first_fill_elements_contact_person(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_lead_contact'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Контактные лица"'},
                                   lang_codes)
    elements.append(element)

    name = 'lead_contact_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_email'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.email.name,
        'field_additional_ordering': 2,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'check_correctness': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'E-mail'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_skype'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.skype.name,
        'field_additional_ordering': 3,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Skype'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_social_network'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.website.name,
        'field_additional_ordering': 4,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Социальная сеть'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_messenger'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.other.name,
        'field_type_other': 'onerowLong',
        'field_additional_ordering': 5,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Мессенджер'}, lang_codes)
    elements.append(element)


# Alias: ПриНачальномЗаполненииЭлементовОрганизации
def on_first_fill_elements_organization(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_organization'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Организации"'},
                                   lang_codes)
    elements.append(element)

    name = 'organization_legal_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['organization']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Юр. адрес'}, lang_codes)
    elements.append(element)

    name = 'organization_actual_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['organization']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 2,
        'can_change_edit_type': True,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Факт. адрес'}, lang_codes)
    elements.append(element)

    name = 'organization_postal_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['organization']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 3,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Почтовый адрес'}, lang_codes)
    elements.append(element)

    name = 'organization_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['organization']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 4,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'}, lang_codes)
    elements.append(element)

    name = 'organization_email'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['organization']['__id__'],
        'type': ContactInfoType.email.name,
        'field_additional_ordering': 5,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'check_correctness': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'E-mail'}, lang_codes)
    elements.append(element)

    name = 'organization_website'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['organization']['__id__'],
        'type': ContactInfoType.website.name,
        'field_additional_ordering': 6,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Сайт'}, lang_codes)
    elements.append(element)

    name = 'organization_fax'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['organization']['__id__'],
        'type': ContactInfoType.fax.name,
        'field_additional_ordering': 7,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Факс'}, lang_codes)
    elements.append(element)

    name = 'organization_other_information'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['organization']['__id__'],
        'type': ContactInfoType.other.name,
        'field_type_other': 'onerowLong',
        'field_additional_ordering': 8,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Другое'}, lang_codes)
    elements.append(element)


# Alias: ПриНачальномЗаполненииЭлементовФизическиеЛица
def on_first_fill_elements_individual(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_individual'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Физические лица"'},
                                   lang_codes)
    elements.append(element)

    name = 'individual_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'}, lang_codes)
    elements.append(element)

    name = 'individual_address_by_registration'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 2,
        'can_change_edit_type': False,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': True,
        'is_using': name not in unused_contact_info,
        'only_national_address': True,
        'check_correctness': True,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'По прописке'}, lang_codes)
    elements.append(element)

    name = 'individual_address_of_residence'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 3,
        'can_change_edit_type': False,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': True,
        'is_using': name not in unused_contact_info,
        'only_national_address': True,
        'check_correctness': True,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Проживание'}, lang_codes)
    elements.append(element)

    name = 'individual_address_for_information'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 4,
        'can_change_edit_type': False,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': True,
        'is_using': name not in unused_contact_info,
        'only_national_address': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Для информирования'}, lang_codes)
    elements.append(element)

    name = 'individual_address_outside_russia'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 5,
        'can_change_edit_type': False,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'За пределами РФ'}, lang_codes)
    elements.append(element)

    name = 'individual_email'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.email.name,
        'field_additional_ordering': 6,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'check_correctness': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Email'}, lang_codes)
    elements.append(element)

    name = 'individual_other_information'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.other.name,
        'field_type_other': 'onerowLong',
        'field_additional_ordering': 7,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Другое'}, lang_codes)
    elements.append(element)

    # BSHRB
    name = 'individual_home_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 8,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Домашний телефон'}, lang_codes)
    elements.append(element)

    name = 'individual_work_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 9,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Рабочий телефон'}, lang_codes)
    elements.append(element)

    name = 'individual_mobile_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['individual']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 10,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Мобильный телефон'}, lang_codes)
    elements.append(element)
    # BSHRB end


# Alias: ПриНачальномЗаполненииЭлементовСтруктурныеЕдиницы
def on_first_fill_elements_structural_unit(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_structural_unit'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Структурные единицы"'}, lang_codes)
    elements.append(element)

    name = 'structural_unit_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['structural_unit']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'}, lang_codes)
    elements.append(element)

    name ='structural_actual_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['structural_unit']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 2,
        'can_change_edit_type': True,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': True,
        'check_correctness': True,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Факт. адрес'}, lang_codes)
    elements.append(element)


# Alias: ПриНачальномЗаполненииЭлементовПользователи
def on_first_fill_elements_user(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_user'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Пользователи"'}, lang_codes)
    elements.append(element)

    name = 'user_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['user']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'}, lang_codes)
    elements.append(element)

    name = 'user_email'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['user']['__id__'],
        'type': ContactInfoType.email.name,
        'field_additional_ordering': 2,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'check_correctness': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'E-mail'}, lang_codes)
    elements.append(element)

    name = 'user_website'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['user']['__id__'],
        'type': ContactInfoType.website.name,
        'field_additional_ordering': 3,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Сайт'}, lang_codes)
    elements.append(element)


# Alias: ПриНачальномЗаполненииЭлементовВидыДеятельностиЕНВД
def on_first_fill_elements_envd_activity_type(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_activity_type'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Виды деятельности ЕНВД"'}, lang_codes)
    elements.append(element)

    name = 'envd_address_activity'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['activity_type']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': True,
        'is_using': name not in unused_contact_info,
        'only_national_address': True,
        'check_correctness': True,
        'hide_irrelevant_addresses': True,
        'include_country_to_view': False
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Место осуществления деятельности'}, lang_codes)
    elements.append(element)


# Alias: ПриНачальномЗаполненииЭлементовТорговыеТочки
def on_first_fill_elements_trade_point(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_trade_point'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Торговые точки"'}, lang_codes)
    elements.append(element)

    name = 'trade_point_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['trade_point']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': True,
        'is_using': name not in unused_contact_info,
        'only_national_address': True,
        'check_correctness': True,
        'hide_irrelevant_addresses': True,
        'include_country_to_view': False,
        'set_oktmo': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Адрес торговой точки'}, lang_codes)
    elements.append(element)


# Alias: ПриНачальномЗаполненииЭлементовЛиды
def on_first_fill_elements_lead(lang_codes: list[str], elements: list[dict], table_parts: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_lead'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Лиды"'}, lang_codes)
    elements.append(element)

    name = 'lead_company_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'}, lang_codes)
    elements.append(element)

    name = 'lead_company_email'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead']['__id__'],
        'type': ContactInfoType.email.name,
        'field_additional_ordering': 2,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'check_correctness': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'E-mail'}, lang_codes)
    elements.append(element)

    name = 'lead_company_legal_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 3,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Юр. адрес'}, lang_codes)
    elements.append(element)

    name = 'lead_company_actual_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 4,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': False,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Факт. адрес'}, lang_codes)
    elements.append(element)

    name = 'lead_company_skype'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead']['__id__'],
        'type': ContactInfoType.skype.name,
        'field_additional_ordering': 5,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Skype'}, lang_codes)
    elements.append(element)

    name = 'lead_company_website'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead']['__id__'],
        'type': ContactInfoType.website.name,
        'field_additional_ordering': 6,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Сайт'}, lang_codes)
    elements.append(element)

    name = 'lead_company_other_information'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead']['__id__'],
        'type': ContactInfoType.other.name,
        'field_type_other': 'onerowLong',
        'field_additional_ordering': 7,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Другое'}, lang_codes)
    elements.append(element)


# Alias: ПриНачальномЗаполненииЭлементовКонтактыЛидов
def on_first_fill_elements_lead_contact(lang_codes: list[str], elements: list[dict], table_name: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_lead_contact'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Контакты лидов"'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_phone'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.phone.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'phone_with_extension': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_email'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.email.name,
        'field_additional_ordering': 2,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
        'check_correctness': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'E-mail'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_skype'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.skype.name,
        'field_additional_ordering': 3,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Skype'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_social_network'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.website.name,
        'field_additional_ordering': 4,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Социальная сеть'}, lang_codes)
    elements.append(element)

    name = 'lead_contact_messenger'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['lead_contact']['__id__'],
        'type': ContactInfoType.other.name,
        'field_type_other': 'onerowLong',
        'field_additional_ordering': 5,
        'can_change_edit_type': True,
        'edit_view': 'input_field',
        'is_required': False,
        'allow_several_values': True,
        'permit_edit_to_user': False,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Мессенджер'}, lang_codes)
    elements.append(element)


# Alias: ПриНачальномЗаполненииЭлементовПунктыВыдачиЗаказа
def on_first_fill_elements_order_pickup_point(lang_codes: list[str], elements: list[dict], table_name: dict):
    unused_contact_info = get_unused_contact_info()

    name = 'directory_order_pickup_point'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'is_group': True,
        'is_using': name not in unused_contact_info,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Пункты выдачи заказа"'}, lang_codes)
    elements.append(element)

    name = 'order_pickup_point_address'
    element = {
        'predefined_type_name': name,
        'predefined_name': name,
        'parent_id': CONTACT_INFO_PD['order_pickup_point']['__id__'],
        'type': ContactInfoType.address.name,
        'field_additional_ordering': 1,
        'can_change_edit_type': True,
        'edit_view': 'dialog',
        'is_required': False,
        'allow_several_values': False,
        'permit_edit_to_user': True,
        'is_using': name not in unused_contact_info,
        'only_national_address': False,
        'check_correctness': False,
        'hide_irrelevant_addresses': False,
        'include_country_to_view': True,
    }
    multilang.fill_multilang_field(element, 'name', {'ru': 'Адрес'}, lang_codes)
    elements.append(element)


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
