import click
from fiddup.views import refine_inputs
from fiddup.fiddup import run_assistant, run_hashmode


@click.command()
@click.option(
    "--inpath",
    "-i",
    type=str,
    required=True,
    help="Path to scan for duplicates.",
)
@click.option(
    "--assistant",
    "-a",
    is_flag=True,
    help="Toggles Assistant mode (name similarity search).",
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
@click.option(
    "--hashmode",
    "-h",
    is_flag=True,
    help="Toggles hash mode (file hash comparison).",
)
@click.option(
    "--chunk_count",
    type=int,
    default=5,
    help="Number of chunks to read from files while hashing. "
         "Higher = more accuracy = Slower.",
)
def main(
    verbose,
    extensions,
    directory: bool = True,
    inpath: str = None,
    assistant: bool = True,
    hashmode: bool = False,
    threshold: float = 0.7,
    chunk_count: int = 5,
):
    """Fiddup is a Non-destructive file deduplicator that can assist you
    to find similar or duplicate files."""
    (
        verbose,
        extensions,
        directory,
        inpath,
        assistant,
        hashmode,
        threshold,
        chunk_count,
    ) = refine_inputs(
        verbose,
        extensions,
        directory,
        inpath,
        assistant,
        hashmode,
        threshold,
        chunk_count,
    )

    if hashmode:
        run_hashmode(verbose, extensions, inpath, chunk_count)

    if assistant:
        run_assistant(verbose, extensions, directory, inpath, threshold)


if __name__ == "__main__":
    main()
