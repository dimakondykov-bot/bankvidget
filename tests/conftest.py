import pytest


@pytest.fixture()
def card_number() -> list:
    return ["1234567890123456", "5555444433332222"]


@pytest.fixture()
def date() -> str:
    return "2025-11-30T17:23:50"


@pytest.fixture
def sample_data() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-02-20T14:45:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-10T09:15:00"},
    ]
