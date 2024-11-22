"""CLI for motheme."""

from collections.abc import Generator
from contextlib import contextmanager, redirect_stdout
from io import StringIO
from pathlib import Path

import arguably

from motheme.apply_theme import apply_theme
from motheme.clear_theme import clear_theme
from motheme.current_theme import current_theme
from motheme.list_themes import list_themes
from motheme.theme_downloader import download_themes
from motheme.util import is_marimo_file


@contextmanager
def quiet_mode(*, enabled: bool = True) -> Generator[None, None, None]:
    """Enable or disable quiet mode."""
    if enabled:
        null_io = StringIO()
        with redirect_stdout(null_io):
            yield
    else:
        yield


def _expand_files(*files: str, recursive: bool) -> list[str]:
    """
    Expand file paths, optionally recursively for directories.
    Only includes valid Marimo notebook files.

    Args:
        files: Tuple of file/directory paths
        recursive: If True, recursively search directories for Python files

    Returns:
        List of expanded file paths that are Marimo notebooks

    """
    if not recursive:
        return [f for f in files if is_marimo_file(f)]

    expanded_files = []
    for file in files:
        path = Path(file)
        if path.is_dir():
            # Find all .py files and filter for Marimo notebooks
            expanded_files.extend(
                str(f) for f in path.rglob("*.py") if is_marimo_file(str(f))
            )
        elif is_marimo_file(str(path)):
            expanded_files.append(str(path))
    return expanded_files


def _check_files_provided(
    action_description: str, files: tuple[str, ...]
) -> bool:
    """
    Check if files were provided and print error message if not.

    Args:
        action_description: Description of the action being performed
        files: Tuple of file/directory paths

    Returns:
        bool: True if files were provided, False otherwise

    """
    if not files:
        print(
            f"Error: Please specify at least one file or directory "
            f"to {action_description}."
        )
        return False
    return True


@arguably.command
def update() -> None:
    """Update Marimo themes from GitHub repository."""
    download_themes()


@arguably.command
def themes() -> None:
    """List available Marimo themes."""
    list_themes()


@arguably.command
def apply(
    theme_name: str,
    *files: str,
    recursive: bool = False,
    quiet: bool = False,
) -> None:
    """
    Apply a Marimo theme to specified notebook files.

    Args:
        theme_name: Name of the theme to apply
        files: Tuple of file/directory paths
        recursive: [-r] If True, recursively search directories for
            Marimo notebooks
        quiet: [-q] If True, suppress output

    """
    if not _check_files_provided("apply the theme", files):
        return

    with quiet_mode(enabled=quiet):
        apply_theme(theme_name, _expand_files(*files, recursive=recursive))


@arguably.command
def clear(*files: str, recursive: bool = False, quiet: bool = False) -> None:
    """
    Remove theme settings from specified notebook files.

    Args:
        files: Tuple of file/directory paths
        recursive: [-r] If True, recursively search directories for
            Marimo notebooks
        quiet: [-q] If True, suppress output

    """
    if not _check_files_provided("clear themes from", files):
        return

    with quiet_mode(enabled=quiet):
        clear_theme(_expand_files(*files, recursive=recursive))


@arguably.command
def current(*files: str, recursive: bool = False, quiet: bool = False) -> None:
    """
    Show currently applied themes for specified notebook files.

    Args:
        files: Tuple of file/directory paths
        recursive: [-r] If True, recursively search directories for
            Marimo notebooks
        quiet: [-q] If True, suppress output

    """
    if not _check_files_provided("check themes for", files):
        return

    with quiet_mode(enabled=quiet):
        current_theme(_expand_files(*files, recursive=recursive))


def main() -> None:
    """CLI entry point."""
    arguably.run()


if __name__ == "__main__":
    main()
