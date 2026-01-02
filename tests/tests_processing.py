import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),  # Найдёт 2 элемента
    ("CANCELED", 1),  # Найдёт 1 элемент
    ("PENDING", 0),  # Не найдёт ни одного
])
def test_filter_by_state(sample_data: list, state: str, expected_count: str) -> None:
    """тест функции filter_by_state, проверяем"""

    # sample_data автоматически подставится из фикстуры
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count
    # Проверяем, что все элементы имеют правильное состояние
    assert all(item["state"] == state for item in result)


# Тест сортировки с параметризацией
@pytest.mark.parametrize("mode, expected_first", [
    (False, "2024-01-15T10:30:00"),  # По возрастанию - первая дата
    (True, "2024-03-10T09:15:00"),  # По убыванию - последняя дата
])
def test_sort_by_date(sample_data: list, mode: bool, expected_first: str) -> None:
    """тест функции sort_by_date"""

    result = sort_by_date(sample_data, mode=mode)
    assert result[0]["date"] == expected_first
