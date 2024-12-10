import re

date_pattern = re.compile(r"\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2}")
phone_pattern = re.compile(r"^\+7 \d{3} \d{3} \d{2} \d{2}$")
email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def get_data_type(input_data):
    """
    Определяет тип данных для каждого поля входных данных.

      Args:
          input_data (dict): Словарь с полями и их значениями, которые нужно проверить.

      Returns:
          dict: Обновленный словарь с типами данных вместо исходных значений.
      """
    for field_name, field_value in input_data.items():
        if date_pattern.fullmatch(field_value):
            input_data[field_name] = "date"
        elif phone_pattern.fullmatch(field_value):
            input_data[field_name] = "phone"
        elif email_pattern.fullmatch(field_value):
            input_data[field_name] = "email"
        else:
            input_data[field_name] = "text"
    return input_data
