from colorama import Style, Fore
from terminaltables import SingleTable
from fiddup.constants import INFO_PREFIX, ERR_PREFIX
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
    verbose,
    extensions,
    directory,
    inpath,
    assistant,
    hashmode,
    threshold,
    chunk_count,
):

    if assistant and hashmode:
        click.secho(f"{ERR_PREFIX} Cannot have both assistant and hashmode.")
        exit()

    if not assistant and not hashmode:
        click.secho(f"{ERR_PREFIX} Need at least -a or -h, see --help")
        exit()

    extensions = [ext.replace(".", "") for ext in extensions]

    if 0 > threshold or threshold > 1:
        click.secho(
            f"{ERR_PREFIX} Please specify a value from 0.00 to 1.00 for -t"
        )
        exit()

    if hashmode and directory:
        click.secho(
            f"{ERR_PREFIX} Cant use hash mode for directories. "
            f"Remove -d or use assistant mode."
        )
        exit()

    if verbose:
        click.secho(f"{INFO_PREFIX} Starting with assistant: {assistant}")
        click.secho(
            f"{INFO_PREFIX} Starting with match threshold: {threshold}"
        )
        click.secho(
            f"{INFO_PREFIX} Scanning for extensions: {', '.join(extensions)}"
        )
        click.secho(f"{INFO_PREFIX} Starting with directory: {directory}")
        click.secho(f"{INFO_PREFIX} Starting with inpath: {inpath}")
        click.secho(f"{INFO_PREFIX} Starting with hashmode: {hashmode}")

    return (
        verbose,
        extensions,
        directory,
        inpath,
        assistant,
        hashmode,
        threshold,
        chunk_count,
    )
