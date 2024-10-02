# Alias: УправлениеКонтактнойИнформациейСлужебныйПовтИсп

# Alias: ДоступенМодульЛокалиации
def is_available_module_localization():
    return metadata.modules.find('base.contact_info.management.localization') is not None

# Alias: ДоступныМодулиРаботаСАдресами
def is_available_modules_addresses():
    return metadata.modules.find('base.contact_info.addresses') is not None
