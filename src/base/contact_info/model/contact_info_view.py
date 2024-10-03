from main import db
from src.base.contact_info.model.contact_info_type import ContactInfoType
from src.base.contact_info.module.management import impl as management_impl
from src.base.contact_info.model.formula import *
from src.base.contact_info.module.management.internal import management as management_internal

# PREDEFINED
CONTACT_INFO_PD = {
    'activity_type': { # Виды деятельности ЕНВД
        '__id__': 1,
        'envd_address_activity': 2,
    },
    'contact_person': { # Контактные лица
        '__id__': 3,
        'email': 4,
        'skype': 5,
        'messenger': 6,
        'social_network': 7,
        'phone': 8,
    },
    'lead_contact': { # Контакты лидов
        '__id__': 9,
        'email': 10,
        'skype': 11,
        'messenger': 12,
        'social_network': 13,
        'phone': 14,
    },
    'counterparty': { # Контрагенты
        '__id__': 15,
        'email': 16,
        'skype': 17,
        'delivery_address': 18,
        'other_information': 19,
        'postal_address': 20,
        'website': 21,
        'phone': 22,
        'fax': 23,
        'actual_address': 24,
        'legal_address': 25,
    },
    'lead': { # Лиды
        '__id__': 26,
        '_lead_contact': {
            '__id__': 27,
            '_email': 28,
            '_skype': 29,
            '_messenger': 30,
            '_social_network': 31,
            '_phone': 32,
        },
        'email': 33,
        'skype': 34,
        'other_information': 35,
        'website': 36,
        'phone': 37,
        'actual_address': 38,
        'legal_address': 39,
    },
    'organization': {
        '__id__': 40,
        'email': 41,
        'other_information': 42,
        'postal_address': 43,
        'website': 44,
        'phone': 45,
        'fax': 46,
        'actual_address': 47,
        'legal_address': 48,
    },
    'user': {
        '__id__': 49,
        'email': 50,
        'website': 51,
        'phone': 52,
    },
    'order_pickup_point': {
        '__id__': 53,
        'address': 54,
    },
    'structural_unit': {
        '__id__': 55,
        'phone': 56,
        'actual_address': 57,
    },
    'trade_point': {
        '__id__': 58,
        'address': 59,
    },
    'individual': {
        '__id__': 60,
        'email': 61,
        'address_for_information': 62,
        'home_phone': 63,
        'other_information': 64,
        'address_outside_russia': 65,
        'mobile_phone': 66,
        'address_by_registration': 67,
        'address_of_residence': 68,
        'work_phone': 69,
        'phone': 70,
    },
}

# Alias: ВидыКонтактнойИнформации
class ContactInfoView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    parent_id = db.Column(db.Integer)
    is_group = db.Column(db.Boolean, default=False) # Признак того, что это группа
    deleted = db.Column(db.Boolean, default=False)
    predefined = db.Column(db.Boolean, default=False)
    predefined_name = db.Column(db.String(150))

    enter_number_by_mask = db.Column(db.Boolean, default=False)
    include_country_to_view = db.Column(db.Boolean, default=False)
    field_type_other = db.Column(db.String(20), default='multirowLong')
    edit_type = db.Column(db.String(20))
    permit_edit_to_user = db.Column(db.Boolean, default=False)
    formula_identifier = db.Column(db.String(150))
    group_name = db.Column(db.String(150))
    predefined_type_name = db.Column(db.String(150))
    is_using = db.Column(db.Boolean, default=True)
    fix_old_addresses = db.Column(db.Boolean, default=False)
    phone_number_mask = db.Column(db.String(150))
    is_international_address_format = db.Column(db.Boolean, default=False)
    can_change_edit_type = db.Column(db.Boolean, default=True)
    is_required = db.Column(db.Boolean, default=False)
    check_correctness = db.Column(db.Boolean, default=False)
    _check_by_fias = db.Column(db.Boolean, default=False) # Deprecated
    allow_several_values = db.Column(db.Boolean, default=False)
    field_additional_ordering = db.Column(db.Integer(precision=5, scale=0))
    hide_irrelevant_addresses = db.Column(db.Boolean, default=False)
    phone_with_extension = db.Column(db.Boolean, default=False)
    type = db.Column(db.String(20), default='address') # ContactInfoType
    only_national_address = db.Column(db.Boolean, default=False)
    _edit_only_in_dialog = db.Column(db.Boolean, default=False) # Deprecated
    set_oktmo = db.Column(db.Boolean, default=False)
    store_edit_history = db.Column(db.Boolean, default=False)
    show_always = db.Column(db.Boolean, default=True)

    def __init__(self):
        pass

    @staticmethod
    def load(id_):
        return ContactInfoView.query.get(id_)

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def save(self):
        decline = False
        self.before_save(decline)

        if decline:
            print('Error before_save ' + self)
            pass

        self.on_save(decline)
        if decline:
            print('Error on_save' + self)

        self.__save()

    def __save(self):
        db.session.add(self)
        db.session.commit()

    def __delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<ContactInfoView %r>' % self.name

    ###############################################################
    # PLATFORM

    def before_save(self, decline: bool):
        if self.predefined_name.startswith('_'):
            return

        if not self.is_group:
            result = management_internal.check_contact_info_view_fields(self)
            if result['has_errors']:
                decline = True
                raise result['error_text']
            group_name = common.get_object_field_value(ContactInfoView.load(self.parent_id), 'predefined_type_name')
            if len(group_name) == 0:
                group_name = common.get_object_field_value(ContactInfoView.load(self.parent_id), 'predefined_name')

            self.check_formula_identifier(decline)



# Alias: ВидыКонтактнойИнформации.Представление
class ContactInfoViewView(db.Model):
    view_id = db.Column(db.Integer, db.ForeignKey('contact_info_view.id'))
    view = db.relationship('ContactInfoView', backref=db.backref('views', lazy='dynamic'))
    lang_code = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(150))

# Alias: ПриНачальномЗаполненииЭлементов
def on_first_fill_elements(lang_codes: list[str], elements: list[dict], table_parts: dict):
    element = {
        'predefined_name': 'directory_user',
        'is_group': True,
        'is_using': True,
    }
    if common.is_subsystem_exists('base.multilang'):
        module_multilang = common.get_module('src.base.multilang.module.main')
        module_multilang.fill_multilang_field(element, 'name', {'ru': 'Контактная информация справочника "Пользователи"'})
    else:
        element['name'] = 'Контактная информация справочника "Пользователи"'
    elements.append(element)

    element = {
        'predefined_name': 'user_email',
        'type': ContactInfoType.email.name,
        'can_change_edit_type': True,
        'allow_several_values': True,
        'parent_id': CONTACT_INFO_PD['directory_user'],
        'formula_identifier': 'email',
        'edit_view': 'input_field',
        'is_using': True,
        'field_additional_ordering': 2,
        'show_always': True,
    }
    if common.is_subsystem_exists('base.multilang'):
        module_multilang = common.get_module('src.base.multilang.module.main')
        module_multilang.fill_multilang_field(element, 'name', {'ru': 'Электронная почта'})
    else:
        element['name'] = 'Электронная почта'
    elements.append(element)

    element = {
        'predefined_name': 'user_phone',
        'type': ContactInfoType.phone.name,
        'can_change_edit_type': True,
        'parent_id': CONTACT_INFO_PD['directory_user'],
        'formula_identifier': 'phone',
        'is_using': True,
        'edit_view': 'input_field_and_dialog',
        'field_additional_ordering': 1,
        'show_always': True,
    }

    if common.is_subsystem_exists('base.multilang'):
        module_multilang = common.get_module('src.base.multilang.module.main')
        module_multilang.fill_multilang_field(element, 'name', {'ru': 'Телефон'})
    else:
        element['name'] = 'Телефон'
    elements.append(element)

    management_impl.on_first_fill_elements(lang_codes, elements, table_parts)


