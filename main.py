from dotenv import load_dotenv
import src.processing as processing
import src.generators as generators
import src.extractor as extractor
import src.filters as filters
import src.widget as widget
import src.utils as utils

menu = [
    '1. Получить информацию о транзакциях из JSON-файла',
    '2. Получить информацию о транзакциях из CSV-файла',
    '3. Получить информацию о транзакциях из XLSX-файла',
]

statuses = [
    'PENDING',
    'EXECUTED',
    'CANCELED',
]


def main():
    load_dotenv()

    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. \n')
    print('Выберите необходимый пункт меню:')
    for menu_item in menu:
        print(menu_item)

    user_input = input('\n>')

    print(f'Выбран пункт {user_input}\n')
    match user_input:
        case '1':
            print("Для обработки выбран JSON-файл.\n")
            process_transactions(utils.load_transactions('data/operations.json'))
        case '2':
            print("Для обработки выбран CSV-файл.\n")
            process_transactions(extractor.extract_from_csv('data/transactions.csv'))
        case '3':
            print("Для обработки выбран XLSX-файл.\n")
            process_transactions(extractor.extract_from_csv('data/transactions_excel.xlsx'))


def process_transactions(data):
    print('Введите статус, по которому необходимо выполнить фильтрацию. ')
    print('Доступные для фильтровки статусы: ' + ', '.join(statuses))

    user_input = input('\n>').upper()
    while user_input not in statuses:
        print(f'Статус операции "{user_input}" недоступен.')
        print('Введите статус, по которому необходимо выполнить фильтрацию. ')
        print('Доступные для фильтровки статусы: ' + ', '.join(statuses))
        user_input = input('\n>').upper()

    result = processing.filter_by_state(data, user_input)

    user_input = input('Отсортировать операции по дате? Да/Нет\n>').lower()
    if user_input == 'да':
        user_input = input('Отсортировать по возрастанию? Да/Нет\n>').lower()
        if user_input == 'да':
            result = processing.sort_by_date(result)
        else:
            result = processing.sort_by_date(result, True)

    user_input = input('Выводить только рублевые транзакции? Да/Нет\n>').lower()
    if user_input == 'да':
        result = list(generators.filter_by_currency(result, 'RUB'))

    user_input = input('Отфильтровать список транзакций по определенному слову '
                       'в описании? Да/Нет\n>').lower()
    if user_input == 'да':
        keyword = input('Введите слово для поиска в описании: ')
        result = filters.filter_operations_by_description(result, keyword)

    print('Распечатываю итоговый список транзакций...')

    if not result:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        return

    print(f'Всего банковских операций в выборке: {len(result)}')
    for operation in result:
        masked_from = operation.get('from')

        if masked_from != '':
            masked_from = widget.mask_account_card(masked_from)

        masked_to = widget.mask_account_card(operation.get('to'))
        amount_transaction = utils.get_amount_from_transaction(operation)

        print(f'{widget.get_date(operation.get("date"))} {operation.get("description")}')
        print(f'{masked_from} -> {masked_to}')
        print(f'Сумма: {amount_transaction}')


if __name__ == '__main__':
    main()
