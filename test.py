# def first_method(l):
#     l.append({'type': 'foo'})
#
# def second_method(l):
#     l.append({'type': 'bar'})
#
# l = []
# first_method(l)
# second_method(l)
#
# print(l) # Works!

# Alias: ИдентификаторДляФормул
def get_formula_identifier(view_str: str):
    """
    Calculates identifier value from view string corresponding to variable naming rules.
    :param view_str: name, string that needs to get from identifier.
    :return: identifier corresponding to variable naming rules.
    """
    special_chars = get_special_chars()

    identifier = ''
    was_special_char = False

    for i in range(len(view_str)):
        char = view_str[i]

        if char in special_chars:
            was_special_char = True
            if char == '_':
                identifier += char
        elif was_special_char or i == 0:
            was_special_char = False
            identifier += char.upper()
        else:
            identifier += char

    return identifier

def get_special_chars():
    ranges = [
        {'min': 0, 'max': 32},
        {'min': 127, 'max': 191}
    ]

    special_chars = list(" .,+,-,/,*,?,=,<,>,(,)%!@#$%&*""№:;{}[]?()\|/`~'^_")
    for range_ in ranges:
        for symbol_code in range(range_['min'], range_['max'] + 1):
            special_chars.append(chr(symbol_code))

    return special_chars

print(get_formula_identifier("this:should:be:a:variable)()*(*)(*)(&+(*$$@%%@%@%@%@%@^#&#&"))