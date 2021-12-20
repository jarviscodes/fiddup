import click
from fiddup.views import refine_inputs
from fiddup.fiddup import run_assistant, run_hashmode


@click.group()
def main():
    click.secho("Fiddup v3.0.0")


@main.command()
@click.option(
    "--in_path",
    "-i",
    type=str,
    required=True,
    help="Path to scan for duplicates.",
)
@click.option(
    "--threshold",
    "-t",
    type=float,
    default=0.7,
    help="Similarity threshold. Assistant will only show similarities > this.",
)
@click.option(
    "--extensions",
    "-e",
    multiple=True,
    required=True,
    help="List of extensions to scan for. "
         "Specify multiple with e.g.: -e zip -e txt -e pdf.",
)
@click.option(
    "--directory",
    "-d",
    is_flag=True,
    help="Include directories in comparison. "
         "Only available in assistant mode.",
)
@click.option("--verbose", "-v", is_flag=True, help="Show verbose output.")
def assistant(verbose, extensions, directory: bool = True,
              in_path: str = None, threshold: float = 0.7):
    verbose, extensions, directory, in_path, threshold, _ \
        = refine_inputs(verbose=verbose, extensions=extensions,
                        directory=directory,
                        in_path=in_path, threshold=threshold)

    run_assistant(verbose, extensions, directory, in_path, threshold)


@main.command()
@click.option(
    "--in_path",
    "-i",
    type=str,
    required=True,
    help="Path to scan for duplicates.",
)
@click.option(
    "--extensions",
    "-e",
    multiple=True,
    required=True,
    help="List of extensions to scan for. "
         "Specify multiple with e.g.: -e zip -e txt -e pdf.",
)
@click.option("--verbose", "-v", is_flag=True, help="Show verbose output.")
@click.option(
    "--chunk_count",
    type=int,
    default=5,
    help="Number of chunks to read from files while hashing. "
         "Higher = more accuracy = Slower.",
)
def hashmode(verbose, extensions, in_path: str = None, chunk_count: int = 5):
    verbose, extensions, _, in_path, _, chunk_count \
        = refine_inputs(verbose=verbose, extensions=extensions,
                        in_path=in_path, chunk_count=chunk_count)
    run_hashmode(verbose, extensions, in_path, chunk_count)


if __name__ == "__main__":
    main()
