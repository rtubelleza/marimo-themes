"""Utility functions."""

from pathlib import Path

import appdirs


def validate_theme_exists(theme_name: str, themes_dir: Path) -> Path:
    """Validate theme exists and return its path."""
    css_file_path = themes_dir / f"{theme_name}.css"
    if not css_file_path.exists():
        print(f"Error: Theme file {css_file_path} does not exist.")
        print("Available themes:")
        for theme in themes_dir.glob("*.css"):
            print(f"- {theme.stem}")
        msg = f"Theme {theme_name} not found"
        raise FileNotFoundError(msg)
    return css_file_path


def get_themes_dir() -> Path:
    """Get the themes directory path."""
    themes_dir = Path(appdirs.user_data_dir("mtheme", "marimo")) / "themes"
    if not themes_dir.exists():
        themes_dir.mkdir(parents=True, exist_ok=True)
    return themes_dir


def is_marimo_file(path: str) -> bool:
    """
    Check if a file is a Marimo notebook.

    A file is considered a Marimo notebook if it:
    1. Has .py extension
    2. Has an exact 'import marimo' line
    3. Creates a marimo.App instance
    4. Contains at least one @app.cell decorator
    """
    if not str(path).endswith(".py"):
        return False

    try:
        with Path(path).open("r", encoding="utf-8") as file:
            lines = file.readlines()

            # Check for exact 'import marimo' line
            has_exact_import = "import marimo\n" in lines

            content = "".join(lines)
            has_app = "marimo.App(" in content
            has_cell = "@app.cell" in content

            return has_exact_import and has_app and has_cell
    except OSError:
        return False
