from typing import Any
import csv
import logging
import os
import pandas as pd  # type: ignore

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
            return data

    except UnicodeDecodeError as e:
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
        return data

    except Exception as e:
        error_msg = f"Ошибка при чтении Excel: {e}"
        logger.error(error_msg)
        raise RuntimeError(error_msg)

