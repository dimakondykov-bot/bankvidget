def get_mask_card_number(card_number: str) -> str | None:
    """принимает на вход номер карты в виде числа и возвращает маску номера по правилу"""
    if len(card_number) != 16:
        return None

    groups = []
    for i in range(0, len(card_number), 4):
        groups.append(card_number[i: i + 4])

    return " ".join([groups[0], groups[1][:2] + "**", "****", groups[3]])


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета в виде числа и возвращает маску номера по правилу"""

    return "**" + account_number[-4:]
