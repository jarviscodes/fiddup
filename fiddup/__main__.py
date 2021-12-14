import click
from fiddup.views import refine_inputs
from fiddup.fiddup import run_assistant, run_hashmode


@click.command()
@click.option("--inpath", "-i", type=str, required=True)
@click.option("--assistant", "-a", is_flag=True)
@click.option("--threshold", "-t", type=float, default=0.7)
@click.option("--extensions", "-e", multiple=True, required=True)
@click.option("--directory", "-d", is_flag=True)
@click.option("--verbose", "-v", is_flag=True)
@click.option("--hashmode", "-h", is_flag=True)
def main(
    verbose,
    extensions,
    directory: bool = True,
    inpath: str = None,
    assistant: bool = True,
    hashmode: bool = False,
    threshold: float = 0.7,
):

    (
        verbose,
        extensions,
        directory,
        inpath,
        assistant,
        hashmode,
        threshold,
    ) = refine_inputs(
        verbose, extensions, directory, inpath, assistant, hashmode, threshold
    )

    if hashmode:
        run_hashmode(verbose, extensions, inpath)

    if assistant:
        run_assistant(verbose, extensions, directory, inpath, threshold)


if __name__ == "__main__":
    main()
