"""CLI for motheme."""

import arguably

from motheme.apply_theme import apply_theme
from motheme.clear_theme import clear_theme
from motheme.current_theme import current_theme
from motheme.list_themes import list_themes
from motheme.theme_downloader import download_themes
from motheme.util import (
    check_files_provided,
    expand_files,
    quiet_mode,
)


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
    git_ignore: bool = False,
) -> None:
    """
    Apply a Marimo theme to specified notebook files.


    Args:
        theme_name: Name of the theme to apply
        files: Tuple of file/directory paths
        recursive: [-r] If True, recursively search directories for
            Marimo notebooks
        quiet: [-q] If True, suppress output
        git_ignore: [-i] If True, ignore files that are git ignored

    """
    if not check_files_provided("apply the theme", files):
        return

    with quiet_mode(enabled=quiet):
        apply_theme(
            theme_name,
            expand_files(*files, recursive=recursive, git_ignore=git_ignore),
        )


@arguably.command
def clear(
    *files: str,
    recursive: bool = False,
    quiet: bool = False,
    git_ignore: bool = False,
) -> None:
    """
    Remove theme settings from specified notebook files.

    Args:
        files: Tuple of file/directory paths
        recursive: [-r] If True, recursively search directories for
            Marimo notebooks
        quiet: [-q] If True, suppress output
        git_ignore: [-i] If True, ignore files that are git ignored

    """
    if not check_files_provided("clear themes from", files):
        return

    with quiet_mode(enabled=quiet):
        clear_theme(
            expand_files(*files, recursive=recursive, git_ignore=git_ignore)
        )


@arguably.command
def current(
    *files: str,
    recursive: bool = False,
    quiet: bool = False,
    git_ignore: bool = False,
) -> None:
    """
    Show currently applied themes for specified notebook files.

    Args:
        files: Tuple of file/directory paths
        recursive: [-r] If True, recursively search directories for
            Marimo notebooks
        quiet: [-q] If True, suppress output
        git_ignore: [-i] If True, ignore files that are git ignored

    """
    if not check_files_provided("check themes for", files):
        return

    with quiet_mode(enabled=quiet):
        current_theme(
            expand_files(*files, recursive=recursive, git_ignore=git_ignore)
        )


def main() -> None:
    """CLI entry point."""
    arguably.run()


if __name__ == "__main__":
    main()
