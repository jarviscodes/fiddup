from colorama import Style, Fore
from terminaltables import SingleTable


def prepare_table_header():
    table_data = [
        [f'{Style.BRIGHT}Name{Style.RESET_ALL}', f'{Style.BRIGHT}Compared to{Style.RESET_ALL}', f'{Style.BRIGHT}Similarity{Style.RESET_ALL}'],
    ]

    return table_data


def show_table_data(table_data):
    table = SingleTable(table_data, f"{Fore.LIGHTGREEN_EX}Results{Style.RESET_ALL}")
    table.inner_heading_row_border = False
    table.justify_columns = {0: 'left', 1: 'left', 2: 'right'}
    print(table.table)
