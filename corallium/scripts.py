"""Start the command line program."""

from beartype import beartype

from . import __pkg_name__, __version__


@beartype
def start() -> None:
    """Run the customized Invoke Program."""
    from calcipy.tasks import all_tasks
    from shoal.cli import start_program
    start_program(__pkg_name__, __version__, all_tasks)