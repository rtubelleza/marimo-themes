"""Utility functions."""

import subprocess
from collections.abc import Generator
from contextlib import contextmanager, redirect_stdout
from io import StringIO
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


@contextmanager
def quiet_mode(*, enabled: bool = True) -> Generator[None, None, None]:
    """Enable or disable quiet mode."""
    if enabled:
        null_io = StringIO()
        with redirect_stdout(null_io):
            yield
    else:
        yield


def get_git_tracked_files() -> set[str]:
    """
    Get list of files tracked by git in the current directory.

    Returns:
        Set of tracked file paths relative to current directory.
        Empty set if not in a git repository or on error.

    """
    try:
        output = subprocess.check_output(  # noqa: S603
            ["git", "ls-files"],  # noqa: S607
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return {path.strip() for path in output.splitlines()}
    except (
        subprocess.SubprocessError,
        subprocess.CalledProcessError,
        OSError,
    ):
        print("Error: Not in a git repository")
        return set()


def expand_files(
    *files: str, recursive: bool, git_ignore: bool = False
) -> list[str]:
    """
    Expand file paths, optionally recursively for directories.
    Only includes valid Marimo notebook files.

    Args:
        files: Tuple of file/directory paths
        recursive: If True, recursively search directories for Python files
        git_ignore: If True, skip files that are git ignored

    Returns:
        List of expanded file paths that are Marimo notebooks

    """
    if git_ignore:
        tracked_files = get_git_tracked_files()

    def is_tracked(path: str) -> bool:
        return (
            not git_ignore
            or str(Path(path).resolve().relative_to(Path.cwd()))
            in tracked_files
        )

    if not recursive:
        return [f for f in files if is_marimo_file(f) and is_tracked(f)]

    expanded_files = []
    for file in files:
        path = Path(file)
        if path.is_dir():
            # Find all .py files and filter for Marimo notebooks
            expanded_files.extend(
                str(f)
                for f in path.rglob("*.py")
                if is_marimo_file(str(f)) and is_tracked(str(f))
            )
        elif is_marimo_file(str(path)) and is_tracked(str(path)):
            expanded_files.append(str(path))
    return expanded_files


def check_files_provided(
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
