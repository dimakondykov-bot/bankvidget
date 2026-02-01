import csv
import logging
import os
from typing import Any

import pandas as pd  # type: ignore

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.propagate = False


def extract_from_csv(path_to_file: str) -> list[dict[str, Any]]:
    """Простое чтение CSV файла в список словарей"""

    if not os.path.exists(path_to_file):
        error_file_path = f'файл не найден {path_to_file}'
        logger.error(error_file_path)
        raise FileNotFoundError(f"Файл не найден: {path_to_file}")

    if not os.path.isfile(path_to_file):
        error_file_path = f'это не файл {path_to_file}'
        logger.error(error_file_path)
        raise ValueError(error_file_path)

    logger.info(f"чтение  CSV файла {path_to_file}")

    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            data = list(reader)

            if not data:
                logger.warning(f'файл {path_to_file} пустой')
                return []

            logger.info(f"Успешно прочитано {len(data)} записей из CSV")
            return convert_csv_or_xlsx_to_json(data)

    except UnicodeDecodeError:
        error_file_path = f"ошибка кодировки {path_to_file}"
        logger.error(error_file_path)
        raise RuntimeError(error_file_path)


def extract_from_xlsx(path_to_file: str) -> list[dict[str, Any]]:
    """Чтение XLSX файла в список словарей"""

    if not os.path.exists(path_to_file):
        error_file_path = f'файл не найден {path_to_file}'
        logger.error(error_file_path)
        raise FileNotFoundError(f"Файл не найден: {path_to_file}")

    if not os.path.isfile(path_to_file):
        error_file_path = f'это не файл {path_to_file}'
        logger.error(error_file_path)
        raise ValueError(error_file_path)

    logger.info(f"чтение Excel файла: {path_to_file}")

    try:
        df = pd.read_excel(path_to_file)

        if df.empty:
            logger.warning(f'файл {path_to_file} пустой')
            return []

        data: list[dict[str, Any]] = df.to_dict('records')

        for row in data:
            for key, value in row.items():
                if pd.isna(value):
                    row[key] = None

        logger.info(f"Успешно прочитано {len(data)} записей")
        return convert_csv_or_xlsx_to_json(data)

    except Exception as e:
        error_msg = f"Ошибка при чтении Excel: {e}"
        logger.error(error_msg)
        raise RuntimeError(error_msg)


def convert_csv_or_xlsx_to_json(content) -> list[dict[str, Any]]:
    unified_data = []

    for item in content:
        operation_amount = {
            "amount": str(item.get("amount", "")),
            "currency": {
                "name": item.get("currency_name", ""),
                "code": item.get("currency_code", "")
            }
        }

        unified_item = {
            "id": int(item.get("id", 0)) if item.get("id") else 0,
            "state": item.get("state", ""),
            "date": item.get("date", ""),
            "operationAmount": operation_amount,
            "description": item.get("description", ""),
            "from": item.get("from", None),
            "to": item.get("to", "")
        }

        unified_data.append(unified_item)

    logger.info(f"Конвертировано {len(unified_data)} записей в унифицированный формат")
    return unified_data
