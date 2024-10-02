# Alias: СтроковыеФункции

# Alias: ПоставитьПараметрыВСтроку
def str_format(tmpl_str: str, *params) -> str:
  '''
  Substitutes parameters into a string template.

  Parameters:
    tmpl_str (str): The string template with placeholders in the format "%<number>".
    *params (str): A variable number of string parameters to substitute into the template.

  Returns:
    str: The resulting string with the substituted values.

  Example:
  >>> result = str_format("%1 goes to %2", "Vasya", "Zoo")
  >>> print(result)  # Output: "Vasya goes to Zoo"
  '''
  if any('%' in param for param in params):
    return format_with_percentage(tmpl_str, *params)
  
  for i, param in enumerate(params, start=1):
    tmpl_str = tmpl_str.replace(f'%{i}', param)
  
  return tmpl_str

# Alias: ПодставитьПараметрыВСтрокуИзМассива
def str_format_arr(tmpl_str: str, params: list) -> str:
  '''
  Substitutes parameters into a string template.

  Parameters:
    tmpl_str (str): The string template with placeholders in the format "%<number>".
    params (list): A list of values to substitute into the template.

  Returns:
    str: The resulting string with the substituted values.
  
  Example:
  >>> params = ["Vasya", "Zoo"]
  >>> result = str_format_arr("%1 goes to %2", params)
  >>> print(result)  # Output: "Vasya goes to Zoo"
  '''
  result = tmpl_str

  for i, val in enumerate(reversed(params), start=1):
    if val:
      result = result.replace("f%{i}", val)
  
  return result

# Alias: ТолькоЦифрыВСтроке
def is_only_digits_in_string(s: (str | any), deprecated: bool = True, space_disallowed: bool = True) -> bool:
  if type(str) != str:
    return False
  
  if not space_disallowed:
    s = s.replace(" ", "")
  
  if len(s) == 0:
    return True
  
  # Если содержит только цифры, то в результате замен должна быть получена пустая строка.
  return len(s.replace("0", "").replace("1", "").replace("2", "").replace("3", "")
             .replace("4", "").replace("5", "").replace("6", "").replace("7", "")
             .replace("8", "").replace("9", "")) == 0

# Alias: ПодставитьПараметрыСПроцентом
def format_with_percentage(s: str, *params) -> str:
  '''
  Substitutes parameters into a string template, considering that the parameters may contain placeholders %1, %2, etc.

  Parameters:
    s (str): The string template with placeholders in the format "%<number>".
    *params (str): A variable number of string parameters to substitute into the template.
  
  Returns:
    str: The resulting string with the substituted values.
  '''
  result = ""
  position = s.find("%")
  while position > -1:
    result += s[:position]
    symbol_after_percent = s[position + 1]
    try:
      substitutable_param = params[int(symbol_after_percent) - 1]
    except (IndexError, ValueError):
      substitutable_param = None
    
    if substitutable_param is None:
      result += "%"
      s = s[position + 1:]
    else:
      result += substitutable_param
      s += s[position + 2:]
    position = s.find("%")
  result += s
  return result