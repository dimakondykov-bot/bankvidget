from src.generators import card_number_generator, transaction_descriptions


def test_first_card_number() -> None:
    """
    Тест 1: Проверяем, что первая карта имеет правильный формат
    """

    generator = card_number_generator(1, 3)
    first_card = next(generator)
    assert first_card == "0000 0000 0000 0001"


def test_three_cards() -> None:
    """
    Тест 2: Проверяем генерацию нескольких карт
    """
    generator = card_number_generator(1, 3)
    cards = list(generator)
    assert len(cards) == 3
    assert cards[0] == "0000 0000 0000 0001"
    assert cards[1] == "0000 0000 0000 0002"
    assert cards[2] == "0000 0000 0000 0003"


def test_transaction_descriptions_basic():
    """
    Тест проверяет, что генератор корректно возвращает описания транзакций.
    """
    # Подготовка тестовых данных
    test_transactions = [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Перевод со счета на счет", "amount": 200},
        {"description": "Оплата услуг", "amount": 300}
    ]
    descriptions_gen = transaction_descriptions(test_transactions)
    descriptions_list = list(descriptions_gen)
    expected_descriptions = ["Перевод организации", "Перевод со счета на счет", "Оплата услуг"]

    assert descriptions_list == expected_descriptions, \
        f"Ожидалось {expected_descriptions}, но получено {descriptions_list}"
