import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", encoding='utf-8', mode='w')
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str | None:
    """принимает на вход номер карты в виде числа и возвращает маску номера по правилу"""

    if len(card_number) != 16:  # проверяет длину номера карты и возвращает None, если она не равна 16 символам
        logger.info('проверяем длину номера карты')

        logger.error(f'ошибка длины номера карты: {len(card_number)}')
        return None

    if not card_number.isdigit():  # проверка формата карты, если содержит не только цифры
        logger.error(f'ошибка формата карты: {card_number}')
        return None

    groups = []
    for i in range(0, len(card_number), 4):  # делаем срез внутри цикла по 4 символа
        logger.info('делаем срез по 4 символа')
        groups.append(card_number[i: i + 4])

    # объединяем по пробелам и делаем маску карты
    logger.info('объединяем по пробелам и делаем маску')
    return " ".join([groups[0], groups[1][:2] + "**", "****", groups[3]])


def get_mask_account(account_number: str) -> str | None:
    """принимает на вход номер счета в виде числа и возвращает маску номера по правилу"""

    if not account_number.isdigit():
        logger.error(f'ошибка формата номера счёта: {account_number}')
        return None

    mask = "**" + account_number[-4:]  # возвращаем маску счёта и последние 4 цифры
    logger.info('возвращает маску счёта по правилу')
    return mask
