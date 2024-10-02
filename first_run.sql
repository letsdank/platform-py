CREATE TABLE IF NOT EXISTS world_country(
  id SERIAL PRIMARY KEY NOT NULL,
  code CHARACTER VARYING(3) UNIQUE,
  name CHARACTER VARYING(60) UNIQUE,
  deleted BOOLEAN DEFAULT FALSE,
  predefined BOOLEAN DEFAULT FALSE,
  predefined_name CHARACTER VARYING(60),
  code_alpha2 CHARACTER VARYING(2),
  code_alpha3 CHARACTER VARYING(3),
  is_eaeu BOOLEAN DEFAULT FALSE,
  full_name CHARACTER VARYING(100),
  international_name CHARACTER VARYING(100)
);

INSERT INTO
  world_country (predefined_name, code, name)
VALUES
  ('Russia', '643', 'РОССИЯ');

CREATE TABLE IF NOT EXISTS contact_info_view(
  id SERIAL PRIMARY KEY NOT NULL,
  name CHARACTER VARYING(150) NOT NULL UNIQUE,
  parent_id BIGINT,
  is_group BOOLEAN DEFAULT FALSE,
  deleted BOOLEAN DEFAULT FALSE,
  predefined BOOLEAN DEFAULT FALSE,
  predefined_name CHARACTER VARYING(150),
  enter_number_by_mask BOOLEAN DEFAULT FALSE,
  include_country_to_view BOOLEAN DEFAULT FALSE,
  field_type_other CHARACTER VARYING DEFAULT 'multirowLong',
  edit_type CHARACTER VARYING(20),
  permit_edit_to_user BOOLEAN DEFAULT FALSE,
  formula_identifier CHARACTER VARYING(150),
  group_name CHARACTER VARYING(150),
  predefined_type_name CHARACTER VARYING(150),
  is_using BOOLEAN DEFAULT TRUE,
  fix_old_addresses BOOLEAN DEFAULT FALSE,
  phone_number_mask CHARACTER VARYING(150),
  is_international_address_format BOOLEAN DEFAULT FALSE,
  can_change_edit_type BOOLEAN DEFAULT TRUE,
  is_required BOOLEAN DEFAULT FALSE,
  check_correctness BOOLEAN DEFAULT FALSE,
  _check_by_fias BOOLEAN DEFAULT FALSE,
  allow_several_values BOOLEAN DEFAULT FALSE,
  field_additional_ordering NUMERIC(5, 0),
  hide_irrelevant_addresses BOOLEAN DEFAULT FALSE,
  phone_with_extension BOOLEAN DEFAULT FALSE,
  type CHARACTER VARYING(20) DEFAULT 'address',
  only_national_address BOOLEAN DEFAULT FALSE,
  _edit_only_in_dialog BOOLEAN DEFAULT FALSE,
  set_oktmo BOOLEAN DEFAULT FALSE,
  store_edit_history BOOLEAN DEFAULT FALSE,
  show_always BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS contact_info_view_view(
    view_id BIGINT REFERENCES contact_info_view,
    lang_code CHARACTER VARYING(10) NOT NULL,
    name CHARACTER VARYING(150)
);

INSERT INTO
  contact_info_view (id, is_group, parent_id, predefined_name, name)
VALUES
  (
    (1, TRUE, NULL, 'directory_activity_type', 'Контактная информация справочника "Виды деятельности ЕНВД"'),
    (2, FALSE, 1, 'envd_address_activity', 'Место осуществления деятельности'),

    (3, TRUE, NULL, 'directory_contact_person', 'Контактная информация справочника "Контактные лица"'),
    (4, FALSE, 3, 'contact_person_email', 'E-mail'),
    (5, FALSE, 3, 'contact_person_skype', 'Skype'),
    (6, FALSE, 3, 'contact_person_messenger', 'Мессенджер'),
    (7, FALSE, 3, 'contact_person_social_network', 'Социальная сеть'),
    (8, FALSE, 3, 'contact_person_phone', 'Телефон'),

    (9, TRUE, NULL, 'directory_lead_contact', 'Контактная информация справочника "Контакты лидов"'),
    (10, FALSE, 9, 'lead_contact_email', 'E-mail'),
    (11, FALSE, 9, 'lead_contact_skype', 'Skype'),
    (12, FALSE, 9, 'lead_contact_messenger', 'Мессенджер'),
    (13, FALSE, 9, 'lead_contact_social_network', 'Социальная сеть'),
    (14, FALSE, 9, 'lead_contact_phone', 'Телефон'),

    (15, TRUE, NULL, 'directory_counterparty', 'Контактная информация справочника "Контрагенты"'),
    (16, FALSE, 15, 'counterparty_email', 'E-mail'),
    (17, FALSE, 15, 'counterparty_skype', 'Skype'),
    (18, FALSE, 15, 'counterparty_delivery_address', 'Доставка'),
    (19, FALSE, 15, 'counterparty_other_information', 'Другое'),
    (20, FALSE, 15, 'counterparty_postal_address', 'Почтовый адрес'),
    (21, FALSE, 15, 'counterparty_website', 'Сайт'),
    (22, FALSE, 15, 'counterparty_phone', 'Телефон'),
    (23, FALSE, 15, 'counterparty_fax', 'Факс'),
    (24, FALSE, 15, 'counterparty_actual_address', 'Факт. адрес'),
    (25, FALSE, 15, 'counterparty_legal_address', 'Юр. адрес'),

    (26, TRUE, NULL, 'directory_lead', 'Контактная информация справочника "Лиды"'),
    (27, TRUE, 26, '_directory_lead_contact', 'Контактная информация контактов лида'),
    (28, FALSE, 27, '_lead_email', 'Email'),
    (29, FALSE, 27, '_lead_skype', 'Skype'),
    (30, FALSE, 27, '_lead_messenger', 'Мессенджер'),
    (31, FALSE, 27, '_lead_social_network', 'Социальная сеть'),
    (32, FALSE, 27, '_lead_phone', 'Телефон'),

    (33, FALSE, 26, 'lead_company_email', 'E-mail'),
    (34, FALSE, 26, 'lead_company_skype', 'Skype'),
    (35, FALSE, 26, 'lead_company_other_information', 'Другое'),
    (36, FALSE, 26, 'lead_company_website', 'Сайт'),
    (37, FALSE, 26, 'lead_company_phone', 'Телефон'),
    (38, FALSE, 26, 'lead_company_actual_address', 'Факт. адрес'),
    (39, FALSE, 26, 'lead_company_legal_address', 'Юр. адрес'),

    (40, TRUE, NULL, 'directory_organization', 'Контактная информация справочника "Организации"'),
    (41, FALSE, 40, 'organization_email', 'E-mail'),
    (42, FALSE, 40, 'organization_other_information', 'Другое'),
    (43, FALSE, 40, 'organization_postal_address', 'Почтовый адрес'),
    (44, FALSE, 40, 'organization_website', 'Сайт'),
    (45, FALSE, 40, 'organization_phone', 'Телефон'),
    (46, FALSE, 40, 'organization_fax', 'Факс'),
    (47, FALSE, 40, 'organization_actual_address', 'Факт. адрес'),
    (48, FALSE, 40, 'organization_legal_address', 'Юр. адрес'),

    (49, TRUE, NULL, 'directory_user', 'Контактная информация справочника "Пользователи"'),
    (50, FALSE, 49, 'user_email', 'E-mail'),
    (51, FALSE, 49, 'user_website', 'Сайт'),
    (52, FALSE, 49, 'user_phone', 'Телефон'),

    (53, TRUE, NULL, 'directory_order_pickup_point', 'Контактная информация справочника "Пункты выдачи заказа"'),
    (54, FALSE, 53, 'order_pickup_point_address', 'Адрес'),

    (55, TRUE, NULL, 'directory_structural_unit', 'Контактная информация справочника "Структурные единицы"'),
    (56, FALSE, 55, 'structural_unit_phone', 'Телефон'),
    (57, FALSE, 55, 'structural_unit_actual_address', 'Факт. адрес'),

    (58, TRUE, NULL, 'directory_trade_point', 'Контактная информация справочника "Торговые точки"'),
    (59, FALSE, 58, 'trade_point_address', 'Адрес торговой точки'),

    (60, TRUE, NULL, 'directory_individual', 'Контактная информация справочника "Физические лица"'),
    (61, FALSE, 60, 'individual_email', 'Email'),
    (62, FALSE, 60, 'individual_address_for_information', 'Для информирования'),
    (63, FALSE, 60, 'individual_home_phone', 'Домашний телефон'),
    (64, FALSE, 60, 'individual_other_information', 'Другое'),
    (65, FALSE, 60, 'individual_address_outside_russia', 'За пределами РФ'),
    (66, FALSE, 60, 'individual_mobile_phone', 'Мобильный телефон'),
    (67, FALSE, 60, 'individual_address_by_registration', 'По прописке'),
    (68, FALSE, 60, 'individual_address_of_residence', 'Проживание'),
    (69, FALSE, 60, 'individual_work_phone', 'Рабочий телефон'),
    (70, FALSE, 60, 'individual_phone', 'Телефон')
  );
