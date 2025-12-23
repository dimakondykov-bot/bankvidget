from unittest.mock import patch, Mock

from src.utils import get_amount_from_transaction, load_transactions


def test_get_amount_rub():
    transaction = {
        'operationAmount': {
            'amount': '1000.0',
            'currency': {'code': 'RUB'}
        }
    }

    result = get_amount_from_transaction(transaction)

    assert result == 1000.0


def test_get_amount_usd():
    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {'code': 'USD'}
        }
    }

    mock_response = Mock()
    mock_response.json.return_value = {'result': 8000.0}

    with patch('src.utils.requests.get', return_value=mock_response):
        result = get_amount_from_transaction(transaction)

    assert result == 8000.0


def test_load_transactions():
    result = load_transactions('data/operations.json')

    assert isinstance(result, list)
    assert len(result) > 0
