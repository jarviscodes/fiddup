import glob
import click
from colorama import Fore, Style
from difflib import SequenceMatcher
from pathlib import Path
from alive_progress import alive_bar
from fiddup.views import prepare_table_header, show_table_data
from fiddup.result import FiddupResult


@click.command()
@click.option("--inpath", "-i", type=str, required=True)
@click.option("--analyze", "-a", type=bool, default=True)
@click.option("--threshold", "-t", type=float, default=0.7)
@click.option("--extensions", "-e", multiple=True, default=["mp3", "mp4", "wma"], required=True)
@click.option("--directory", "-d", is_flag=True)
@click.option("--verbose", "-v", is_flag=True)
def main(
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
    table_data = prepare_table_header()

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

    show_table_data(table_data)

if __name__ == "__main__":
    main()
