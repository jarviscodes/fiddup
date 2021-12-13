import glob
import click
from colorama import Fore, Back, Style
from difflib import SequenceMatcher


class FiddupResult(object):
    base_file: str
    compared_file: str
    similarity: float

    def __init__(self, base_file, compared_file, similarity):
        self.base_file = base_file
        self.compared_file = compared_file
        self.similarity = round(similarity * 100, 2)

    def __str__(self):
        return f"{self.base_file: <40}{self.compared_file: <40}{self.similarity: >15}"

    def __eq__(self, other):
        return self.base_file == other.compared_file and self.compared_file == other.base_file


@click.command()
@click.option("--inpath", "-i", type=str, required=True)
@click.option("--analyze", "-a", type=bool, default=True)
@click.option("--threshold", "-t", type=float, default=0.7)
@click.option("--extensions", "-e", multiple=True, default=["mp3", "mp4", "wma"], required=True)
@click.option("--verbose", "-v", is_flag=True)
def fiddup(
    verbose,
    extensions,
    inpath: str = None,
    analyze: bool = True,
    threshold: float = 0.7,
):
    _file_list = []
    _result_list = []

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


    for ext in extensions:
        for file in glob.glob(f"{inpath}\\*.{ext}"):
            _file_list.append(file)

    for file in _file_list:
        for cmpfile in _file_list:
            if file != cmpfile:
                _fu = FiddupResult(
                    base_file=file,
                    compared_file=cmpfile,
                    similarity=SequenceMatcher(None, file, cmpfile).ratio(),
                )
                if _fu.similarity >= threshold * 100:
                    if _fu not in _result_list:
                        _result_list.append(_fu)

    click.secho(f"[{Fore.LIGHTGREEN_EX}Results{Style.RESET_ALL}]")
    click.secho(f"{Style.BRIGHT}{'Original': <40}{'Compared to': <40}{'Match': <15}")
    for result in _result_list:
        click.echo(result)


if __name__ == "__main__":
    fiddup()
