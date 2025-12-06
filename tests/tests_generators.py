import pytest

from src.generators import filter_by_currency, card_number_generator


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
