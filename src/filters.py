import re
import logging
from collections import Counter


def filter_operations_by_description(data: list[dict], search: str) -> list[dict]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей у которых в описании есть данная строка
    """

    filtered_operation = []

    pattern = re.compile(search, re.IGNORECASE)

    for row in data:
        descr = row.get('description', '')

        if pattern.search(descr):
            filtered_operation.append(row)

    return filtered_operation


def count_operations_by_category(operations: list[dict], categories: list) -> dict:
    """
    Функцию принимает список словарей с данными о банковских операциях список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории.
    """

    category_list = []

    for operation in operations:
        category = operation.get('description')
        if category in categories:
            category_list.append(category)

    result = Counter(category_list)

    return dict(result)
