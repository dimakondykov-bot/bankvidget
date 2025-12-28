from typing import Any
import csv
import pandas as pd  # type: ignore


def extract_from_csv(path_to_file: str) -> list[dict[str, Any]]:
    """Простое чтение CSV файла в список словарей"""
    with open(path_to_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)


def extract_from_xlsx(path_to_file: str) -> list[dict[str, Any]]:
    """Чтение XLSX файла в список словарей"""
    df = pd.read_excel(path_to_file)
    data: list[dict[str, Any]] = df.to_dict('records')
    return data
