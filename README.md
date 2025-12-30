# Title:

Widget for a personal account

## Description:

This widget shows several successful banking transactions of the client

## Installing:

1.Clone the repository

```
git clone git@github.com:dimakondykov-bot/bankvidget.git
```

2.Install requirements

```
pip instull -r requirements.txt
```

3.program testing 

```
pytest
```

### adding generator functions

1. tools for efficient work with large volumes of transaction data

#### Added a decorator and decorator testing

1. Logs:
- that the function was called and with what arguments
- that the function returned a result
- if there was an error, it displays the error text

# adding extractor function

1. функция для чтения и преобразование данных из различных форматов таких как CSV и Excel в единый формат данных -
 список словарей.


## Основные функции:

1. Чтение CSV файлов
```

from data_extractor import extract_from_csv

# Простое чтение
data = extract_from_csv("data.csv")

# С указанием параметров
data = extract_from_csv(
    "data.csv",
    delimiter=";",
    encoding="utf-8-sig"
)
```

2. Чтение Excel файлов
```
from data_extractor import extract_from_xlsx

# Чтение первого листа
data = extract_from_xlsx("data.xlsx")

# Чтение конкретного листа и колонок
data = extract_from_xlsx(
    "data.xlsx",
    sheet_name="Отчет",
    use_columns=["Name", "Age", "City"]
```
