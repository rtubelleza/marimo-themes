"""Clear theme from marimo notebooks."""

import re
from pathlib import Path

from .util import is_marimo_file


def clean_app_line(line: str) -> str:
    """
    Remove css_file parameter and cleaning up punctuation.

    Args:
        line: The line containing marimo.App() call.

    Returns:
        Cleaned line with css_file parameter removed and punctuation fixed

    """
    # Remove css_file parameter and its value
    pattern = r',?\s*css_file=(["\'])(?:(?!\1).)*\1'
    new_line = re.sub(pattern, "", line)

    # Clean up any potential double commas or empty parentheses
    new_line = re.sub(r",\s*,", ",", new_line)
    new_line = re.sub(r"\(\s*,", "(", new_line)
    return re.sub(r",\s*\)", ")", new_line)


def process_file(file_name: str) -> tuple[bool, list[str]]:
    """
    Process a single file to remove theme settings.

    Args:
        file_name: Path to the file to process

    Returns:
        Tuple of (success, modified_content)
        - success: True if theme was cleared, False if no theme found
        - modified_content: List of lines with theme removed

    """
    with Path(file_name).open("r") as f:
        content = f.readlines()

    new_content = []
    theme_cleared = False

    for i, line in enumerate(content):
        if "marimo.App(" in line and "css_file=" in line:
            new_line = clean_app_line(line)
            new_content.append(new_line)
            new_content.extend(content[i + 1 :])
            theme_cleared = True
            break
        new_content.append(line)

    return theme_cleared, new_content


def clear_theme(files: list[str]) -> None:
    """
    Remove theme settings from specified notebook files.

    Args:
        files: List of Marimo notebook files to modify

    """
    modified_files = []
    try:
        for file_name in files:
            if not is_marimo_file(file_name):
                print(
                    f"Skipping {file_name} because "
                    "it is not a Marimo notebook."
                )
                continue

            theme_cleared, new_content = process_file(file_name)

            if theme_cleared:
                with Path(file_name).open("w") as f:
                    f.writelines(new_content)
                modified_files.append(file_name)
                print(f"Cleared theme from {file_name}")
            else:
                print(f"No theme found in {file_name}")

    except OSError as e:
        print(f"Error processing {file_name}: {e}")

    # Summary
    if modified_files:
        print(
            f"\nSuccessfully cleared theme from "
            f"{len(modified_files)} file(s)."
        )
    else:
        print("No files were modified.")
