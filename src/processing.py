def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
    """ Filter by 'state' """

    filtered_data = []

    for item in data:
        if item['state'] == state:
            filtered_data.append(item)

    return filtered_data


def sort_by_date(list_data: list, mode: bool = False) -> list:
    """ Sort by 'date' """

    return sorted(list_data, key=lambda item: item['date'], reverse=mode)
