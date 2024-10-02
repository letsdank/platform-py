import enum

# Alias: ТипыКонтактнойИнформации
class ContactInfoType(enum.Enum):
    address = "Адрес"
    phone = "Телефон"
    email = "Адрес электронной почты"
    skype = "Skype"
    website = "Веб-страница"
    fax = "Факс"
    other = "Другое"