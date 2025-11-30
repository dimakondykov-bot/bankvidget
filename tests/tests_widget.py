import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("card_input, expected", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("MasterCard 5555444433332222", "MasterCard 5555 44** **** 2222"),
])
def test_get_mask_account_card(card_input, expected):
    result = mask_account_card(card_input)
    assert result == expected

@pytest.mark.parametrize("expected", ["30.11.2025"])
def test_get_date(date, expected):
    assert get_date(date) == expected
