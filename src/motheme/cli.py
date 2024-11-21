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
def apply(theme_name: str, *files: str, recursive: bool = False) -> None:
    """Apply a Marimo theme to specified notebook files."""
    if not _check_files_provided("apply the theme", files):
        return
    apply_theme(theme_name, _expand_files(*files, recursive=recursive))


@arguably.command
def clear(*files: str, recursive: bool = False) -> None:
    """Remove theme settings from specified notebook files."""
    if not _check_files_provided("clear themes from", files):
        return
    clear_theme(_expand_files(*files, recursive=recursive))


@arguably.command
def current(*files: str, recursive: bool = False) -> None:
    """Show currently applied themes for specified notebook files."""
    if not _check_files_provided("check themes for", files):
        return
    current_theme(_expand_files(*files, recursive=recursive))


def main() -> None:
    """CLI entry point."""
    arguably.run()


if __name__ == "__main__":
    main()
