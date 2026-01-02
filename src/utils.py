import json
import logging
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/app.log", encoding='utf-8', mode='w')
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def load_transactions(path_to_file) -> list:
    """ Функция принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях """
    try:
        logger.info('Загрузка файла json')
        with open(path_to_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"файл {path_to_file} не найден")
        print(f"файл {path_to_file} не найден")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"произошла ошибка JSON файла: {path_to_file}")
        print(f"ошибка JSON файла {path_to_file} {e}")
        return []
    except Exception as e:
        logger.error(f"произошла ошибка при чтении: {e}")
        print(f"ошибка при чтении {path_to_file}: {e}")
        return []


def get_amount_from_transaction(transaction_dict) -> float:
    """ Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float"""
    try:
        operation = transaction_dict.get('operationAmount')
        amount = operation.get('amount')
        currency_code = operation.get('currency').get('code')

        if not operation:
            logger.error('В транзакции нет данных об операции')
            return 0.0

        if amount is None:
            logger.error('В транзакции не указана сумма операции')
            return 0.0

        if currency_code is None:
            logger.error('В транзакции не указан код валюты')
            return float(amount)

        if currency_code != 'RUB':
            headers = {
                "apikey": os.getenv('API_LAYER_KEY'),
            }

            response = requests.get(
                f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}',
                headers=headers
            )
            body = response.json()
            amount = body.get('result')

        return float(amount)
    except Exception as e:
        logger.error(f"Неожиданная ошибка при обработке транзакции: {e}")
        print(f"Неожиданная ошибка при обработке транзакции: {e}")
        return 0.0
