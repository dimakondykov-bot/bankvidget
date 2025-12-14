from typing import Iterator


def filter_by_currency(transactions: list, currency_code: str = "USD") -> Iterator[str]:
    """
    Фильтрует транзакции по указанной валюте.
    Возвращает итератор по транзакциям в указанной валюте.

    Args:
        transactions: Список транзакций
        currency_code: Код валюты (по умолчанию "USD")

    Yields:
        Транзакции, где валюта операции соответствует currency_code
    """
    for transaction in transactions:
        if (transaction.get('operationAmount') and
                transaction['operationAmount'].get('currency') and
                transaction['operationAmount']['currency'].get('code') == currency_code):
            yield transaction


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX

    Args:
        start: начальный номер (без пробелов) от 1 до 9999999999999999
        end: конечный номер (без пробелов) до 9999999999999999
    """

    if not (1 <= start <= end <= 9999999999999999):
        raise ValueError("Некорректный диапазон номеров")

    for number in range(start, end + 1):
        card_str = str(number).zfill(16)
        formatted = f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции.

    Args:
        transactions: Список транзакций.

    Yields:
        Описание каждой транзакции (строка)
    """
    for transaction in transactions:
        description = transaction.get('description', '')
        yield description
