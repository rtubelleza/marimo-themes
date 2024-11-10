"""CLI for motheme."""

from pathlib import Path

import arguably

from .apply_theme import apply_theme
from .theme_downloader import download_themes, list_themes


@arguably.command
def update() -> None:
    """Update Marimo themes from GitHub repository."""
    download_themes()


@arguably.command
def themes() -> None:
    """List available Marimo themes."""
    list_themes()


@arguably.command
def apply(theme_name: str, *files: str, recursive: bool = False) -> None:
    """
    Apply a Marimo theme to specified notebook files.

    Args:
        theme_name: Name of the theme to apply
        files: List of Marimo notebook files to modify
        recursive: [-r] If True, recursively search directories for .mo files

    """
    if not files:
        print(
            "Error: Please specify at least one file or directory "
            "to apply the theme."
        )
        return

    if recursive:
        expanded_files = []
        for file in files:
            if Path(file).is_dir():
                # Recursively find all .mo files in the directory
                expanded_files.extend(Path(file).rglob("*.py"))
            else:
                expanded_files.append(file)
        files = expanded_files

    apply_theme(theme_name, list(files))


def main() -> None:
    """CLI entry point."""
    arguably.run()


if __name__ == "__main__":
    main()
