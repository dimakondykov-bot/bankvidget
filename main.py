from dotenv import load_dotenv
import src.utils as utils


def main():
    load_dotenv()

    print(utils.get_amount_from_transaction({
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "1000.0",
            "currency": {
                "name": "руб.",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }))

    print(utils.load_transactions('D:\\repositories\\test_poetry\\data\\operations.json'))


if __name__ == '__main__':
    main()
