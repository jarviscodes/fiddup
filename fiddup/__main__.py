import glob
import click
from colorama import Fore, Back, Style
from difflib import SequenceMatcher
from pathlib import Path
from alive_progress import alive_bar
from terminaltables import SingleTable


def prepare_table_list():
    table_data = [
        [f'{Style.BRIGHT}Name{Style.RESET_ALL}', f'{Style.BRIGHT}Compared to{Style.RESET_ALL}', f'{Style.BRIGHT}Similarity{Style.RESET_ALL}'],
    ]

    return table_data


class FiddupResult(object):
    base_file: str
    compared_file: str
    similarity: float

    def __init__(self, base_file, compared_file, similarity):
        self.base_file = base_file
        self.compared_file = compared_file
        self.similarity = round(similarity, 2)

    def __str__(self):
        return f"{self.base_file: <40}{self.compared_file: <40}{self.similarity: <15}"

    def __eq__(self, other):
        return self.base_file == other.compared_file and self.compared_file == other.base_file

    def as_terminaltable_row(self):
        return [self.base_file, self.compared_file, self.similarity]


@click.command()
@click.option("--inpath", "-i", type=str, required=True)
@click.option("--analyze", "-a", type=bool, default=True)
@click.option("--threshold", "-t", type=float, default=0.7)
@click.option("--extensions", "-e", multiple=True, default=["mp3", "mp4", "wma"], required=True)
@click.option("--directory", "-d", is_flag=True)
@click.option("--verbose", "-v", is_flag=True)
def fiddup(
        verbose,
        extensions,
        directory: bool = True,
        inpath: str = None,
        analyze: bool = True,
        threshold: float = 0.7,
):
    _file_list = []
    _result_list = []
    _file_count = 0
    _dir_count = 0
    table_data = prepare_table_list()

    if verbose:
        click.secho(
            f"[{Fore.CYAN}Info{Style.RESET_ALL}] Starting with analyze: {analyze}"
        )
        click.secho(
            f"[{Fore.CYAN}Info{Style.RESET_ALL}] Starting with match threshold: {threshold}"
        )
        click.secho(
            f"[{Fore.CYAN}Info{Style.RESET_ALL}] Scanning for extensions: {', '.join(extensions)}"
        )

    if directory:
        # Scan the inpath for entries
        for path in glob.glob(f"{inpath}\\*"):
            ppath = Path(path)
            if ppath.is_dir():
                # Need only last part because it is filename
                _file_list.append(str(*ppath.parts[-1:]))
                _dir_count += 1
        if verbose:
            click.secho(f"[{Fore.CYAN}Info{Style.RESET_ALL}] Found {_dir_count} directories.")

    for ext in extensions:
        # Scan the inpath for the specified extensions
        for file in glob.glob(f"{inpath}\\*.{ext}"):
            ppath = Path(file)
            # Only filename
            _file_list.append(str(*ppath.parts[-1:]))
            _file_count += 1
    if verbose:
        click.secho(f"[{Fore.CYAN}Info{Style.RESET_ALL}] Found {_file_count} files.")

    with alive_bar(_dir_count + _file_count) as bar:
        for file in _file_list:
            for cmpfile in _file_list:
                if file != cmpfile:
                    _fu = FiddupResult(
                        base_file=file,
                        compared_file=cmpfile,
                        similarity=SequenceMatcher(None, file, cmpfile).ratio(),
                    )
                    if _fu.similarity >= threshold:
                        if _fu not in _result_list:
                            table_data.append(_fu.as_terminaltable_row())
                            _result_list.append(_fu)
            bar()

    table = SingleTable(table_data, f"{Fore.LIGHTGREEN_EX}Results{Style.RESET_ALL}")
    table.inner_heading_row_border = False
    table.justify_columns = {0: 'left', 1: 'left', 2: 'right'}
    print(table.table)


if __name__ == "__main__":
    fiddup()
