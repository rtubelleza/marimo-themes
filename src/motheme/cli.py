# src/mtheme/cli.py
from typing import Optional

import arguably


def list_themes() -> None:
    """List available Marimo themes."""
    # TODO: Implement theme listing logic


def update_themes() -> None:
    """Update themes from GitHub repository."""
    # TODO: Implement theme update mechanism


def apply_theme(
    theme_name: str,
    files: Optional[list[str]] = None,
    directory: Optional[str] = None,
) -> None:
    """
    Apply a specific theme to Marimo notebooks.

    :param theme_name: Name of the theme to apply
    :param files: List of specific files to modify
    :param directory: Directory to apply theme recursively
    """
    # TODO: Implement theme application logic


def main() -> None:
    arguably.run()


if __name__ == "__main__":
    main()
