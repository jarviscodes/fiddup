from colorama import Style, Fore
from terminaltables import SingleTable
from fiddup.constants import ERR_PREFIX
import click


def prepare_name_table_header():
    table_data = [
        [
            f"{Style.BRIGHT}Name{Style.RESET_ALL}",
            f"{Style.BRIGHT}Compared to{Style.RESET_ALL}",
            f"{Style.BRIGHT}Similarity{Style.RESET_ALL}",
        ],
    ]

    return table_data


def prepare_hash_table_header():
    table_data = [
        [
            f"{Style.BRIGHT}Name{Style.RESET_ALL}",
            f"{Style.BRIGHT}Compared to{Style.RESET_ALL}",
            f"{Style.BRIGHT}File Hash{Style.RESET_ALL}",
            f"{Style.BRIGHT}File Size{Style.RESET_ALL}"
        ],
    ]

    return table_data


def get_name_table_data(table_data):
    table = SingleTable(
        table_data, f"{Fore.LIGHTGREEN_EX}Results{Style.RESET_ALL}"
    )
    table.inner_heading_row_border = False
    table.justify_columns = {0: "left", 1: "left", 2: "right"}
    return table


def get_hash_table_data(table_data):
    table = SingleTable(
        table_data, f"{Fore.LIGHTGREEN_EX}Results{Style.RESET_ALL}"
    )
    table.inner_heading_row_border = False
    table.justify_columns = {0: "left", 1: "left", 2: "right", 3: "right"}
    return table


def refine_inputs(
    verbose=False,
    extensions=None,
    directory=False,
    in_path=None,
    threshold=0,
    chunk_count=5,
):
    if extensions is None:
        extensions = []

    extensions = [ext.replace(".", "") for ext in extensions]

    if 0 > threshold or threshold > 1:
        click.secho(
            f"{ERR_PREFIX} Please specify a value from 0.00 to 1.00 for -t"
        )
        exit()

    return (
        verbose,
        extensions,
        directory,
        in_path,
        threshold,
        chunk_count,
    )
