"""Apply a Marimo theme to specified notebook files."""

import re
from pathlib import Path

from .util import get_themes_dir, is_marimo_file


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


def modify_app_line(line: str, css_file_path: Path) -> str:
    """Modify a marimo.App line to include or update the css_file parameter."""
    if "css_file=" in line:
        # Replace existing css_file parameter
        return re.sub(
            r'css_file=["\'"][^"\']*["\']', f'css_file="{css_file_path}"', line
        )
    if line.strip().endswith("marimo.App()"):
        # No existing parameters
        return line.replace(
            "marimo.App()", f'marimo.App(css_file="{css_file_path}")'
        )
    # Has existing parameters, insert css_file
    return line.replace(
        "marimo.App(", f'marimo.App(css_file="{css_file_path}", '
    )


def process_file(
    file_path: str, css_file_path: Path
) -> tuple[bool, list[str]]:
    """Process a single file and return (success, new_content)."""
    with Path(file_path).open() as f:
        content = f.readlines()

    new_content = []
    theme_applied = False

    for i, line in enumerate(content):
        if "app = marimo.App(" in line:
            new_line = modify_app_line(line, css_file_path)
            new_content.append(new_line)
            # Append all remaining lines without checking them
            new_content.extend(content[i + 1 :])
            theme_applied = True
            break
        new_content.append(line)

    return theme_applied, new_content


def apply_theme(theme_name: str, files: list[str]) -> None:
    """
    Apply a Marimo theme to specified notebook files.

    :param theme_name: Name of the theme to apply
    :param files: List of Marimo notebook files to modify
    """
    # Validate theme
    themes_dir = get_themes_dir()
    try:
        css_file_path = validate_theme_exists(theme_name, themes_dir)
    except FileNotFoundError:
        return

    # Process files
    modified_files = []
    try:
        for file_name in files:
            if not is_marimo_file(file_name):
                print(
                    f"Skipping {file_name} because "
                    "it is not a Marimo notebook."
                )
                continue

            theme_applied, new_content = process_file(file_name, css_file_path)

            if theme_applied:
                with Path(file_name).open("w") as f:
                    f.writelines(new_content)
                modified_files.append(file_name)
                print(f"Applied {theme_name} theme to {file_name}")
            else:
                print(f"Failed to apply {theme_name} theme to {file_name}")

    except OSError as e:
        print(f"Error processing {file_name}: {e}")

    # Summary
    if modified_files:
        print(
            f"\nSuccessfully applied {theme_name} theme to "
            f"{len(modified_files)} file(s)."
        )
    else:
        print("No files were modified.")
