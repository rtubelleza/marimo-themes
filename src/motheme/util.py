"""Utility functions."""

from pathlib import Path

import appdirs


def get_themes_dir() -> Path:
    """Get the themes directory path."""
    themes_dir = Path(appdirs.user_data_dir("mtheme", "marimo")) / "themes"
    if not themes_dir.exists():
        themes_dir.mkdir(parents=True, exist_ok=True)
    return themes_dir


def is_marimo_file(path: str) -> bool:
    """Check if a file is a Marimo notebook."""
    if not path.endswith(".py"):
        return False

    with Path(path).open("rb") as file:
        return b"app = marimo.App(" in file.read()
