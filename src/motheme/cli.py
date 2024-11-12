"""CLI for motheme."""

from pathlib import Path

import arguably

from .apply_theme import apply_theme
from .clear_theme import clear_theme
from .current_theme import current_theme
from .list_themes import list_themes
from .theme_downloader import download_themes
from .util import is_marimo_file


@arguably.command
def update() -> None:
    """Update Marimo themes from GitHub repository."""
    download_themes()


@arguably.command
def themes() -> None:
    """List available Marimo themes."""
    list_themes()


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


@arguably.command
def apply(theme_name: str, *files: str, recursive: bool = False) -> None:
    """
    Apply a Marimo theme to specified notebook files.

    Args:
        theme_name: Name of the theme to apply
        files: List of Marimo notebook files to modify
        recursive: [-r] If True, recursively search directories for marimo
            notebooks

    """
    if not files:
        print(
            "Error: Please specify at least one file or directory "
            "to apply the theme."
        )
        return

    files = _expand_files(*files, recursive=recursive)
    apply_theme(theme_name, files)


@arguably.command
def clear(*files: str, recursive: bool = False) -> None:
    """
    Remove theme settings from specified notebook files.

    Args:
        files: List of Marimo notebook files to modify
        recursive: [-r] If True, recursively search directories for marimo
            notebooks

    """
    if not files:
        print(
            "Error: Please specify at least one file or directory "
            "to clear themes from."
        )
        return

    files = _expand_files(*files, recursive=recursive)
    clear_theme(files)


@arguably.command
def current(*files: str, recursive: bool = False) -> None:
    """
    Show currently applied themes for specified notebook files.

    Args:
        files: List of Marimo notebook files to check
        recursive: [-r] If True, recursively search directories for marimo
            notebooks

    """
    if not files:
        print(
            "Error: Please specify at least one file or directory "
            "to check themes for."
        )
        return

    files = _expand_files(*files, recursive=recursive)
    current_theme(files)


def main() -> None:
    """CLI entry point."""
    arguably.run()


if __name__ == "__main__":
    main()
