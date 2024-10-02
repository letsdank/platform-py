# Alias: РаботаСАдресами

# Alias: ТаблицаКлассификатора
def get_classifier_table():
    """
    Returns full data of ОКСМ classifier.
    :return:
    """
    classifier = None

    if common.is_subsystem_exists('net_user_support.classifier_manager'):
        classifier_id = get_classifier_id()

        module_classifier_manager = common.get_module('src.net_user_support.module.classifier_manager')
        ids = common.get_value_list(classifier_id)
        result = module_classifier_manager.get_classifiers_files(ids)

        if len(result['error_code']) == 0 and result['classifiers_data'] is not None:
            classifier_description = next(item['id'] == classifier_id for item in result['classifiers_data'])
            if classifier_description is not None:
                classifier = get_from_temp_store(classifier_description['file_address'])

    if classifier is None:
        template = get_template('src/base/contact_info/model/world_country/classifier.xml')
        xml_classifier = template.get_text()
    else:
        with open(classifier, 'r') as file:
            xml_classifier = file.read()

    country_table = xdto_serializer.loads(xml_classifier)

    if 'international_name' not in country_table[0]:
        for country in country_table:
            country['international_name'] = ''

    return country_table

def get_classifier_id():
    return "Countries"