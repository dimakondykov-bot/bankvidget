from src.extractor import extract_from_csv, extract_from_xlsx


def test_extract_from_csv():
    """Простой тест чтения CSV файла"""
    result = extract_from_csv('data/transactions.csv')

    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], dict)


def test_extract_from_xlsx():
    """Простой тест чтения XLSX файла"""
    result = extract_from_xlsx('data/transactions_excel.xlsx')

    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], dict)
