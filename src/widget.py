from __future__ import annotations

from .masks import get_mask_card_number, get_mask_account


def mask_account_card(raw_card_number: str) -> str:
    """Обрабатывает информацию как о картах, так и о счетах"""

    card_number = raw_card_number.split(" ")  # делим принимаемую строку по пробелам

    count_card_number = len(card_number)
    type_card = ' '.join(card_number[:count_card_number - 1])  # Получаем тип карты

    mask: str

    if type_card.lower() == "счет":
        mask = get_mask_account(card_number[-1])  # берём только маску номера счёта
    else:
        card_mask = get_mask_card_number(card_number[-1])  # берём только маску номера карты

        if card_mask is None:
            raise ValueError("Номер карты должен содержать 16 цифр")

        mask = card_mask

    return type_card + ' ' + mask


def get_date(date: str) -> str:
    """функция принимает строку с датой и возвращает с датой в формате 'ДД.ММ.ГГГГ' """

    separated_date = date.split("T")  # Делим строку по символу 'Т'
    date_str = separated_date[0]
    new_date_str = date_str[8:10] + "." + date_str[5:7] + "." + date_str[:4]  # делаем срез даты в формате 'ДД.ММ.ГГГГ'

    return new_date_str
