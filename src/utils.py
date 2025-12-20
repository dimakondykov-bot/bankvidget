import json
import os
import requests


def load_transactions(path_to_file) -> list:
    """ Функция принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях """
    try:
        with open(path_to_file, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        parsed_data = []
        if isinstance(parsed_data, list):
            return parsed_data
        else:
            return []


def get_amount_from_transaction(transaction_dict) -> float:
    """ Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float"""
    operation = transaction_dict.get('operationAmount')
    amount = operation.get('amount')
    currency_code = operation.get('currency').get('code')

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
