from typing import Any, Generator, List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[dict, Any, None] | None:
    """
    Filter transactions by currency.Фильтрует транзакции по валюте.

Args:
    transactions: Список словарей с транзакциями
    currency: Код валюты для фильтрации (например, 'USD', 'EUR')
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions должен быть списком")

    if not currency:
        raise ValueError("currency не может быть пустым")

    for transaction in transactions:
        if not isinstance(transactions, list):
            continue
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            return (transaction for transaction in transactions
                    if transaction.get("operationAmount", {}).get("currency", {}).get(
                "code").upper() == currency.upper())
    return None


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Generator[str, Any, None]:
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
