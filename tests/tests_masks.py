import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("1234567891011121", "1234 56** **** 1121"),
    ("123456 7891011121", None), ])
def test_get_mask_card_number(card_number: str, expected: str | None) -> None:
    """Тестирование функции get_mask_card_number, проверка входных данны карты"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number, expected", [("8034687658648974", "**8974")])
def test_get_mask_account(card_number: str, expected: str) -> None:
    """Тестирование функции get_mask_account, проверка входных данных счёта"""
    assert get_mask_account(card_number) == expected
