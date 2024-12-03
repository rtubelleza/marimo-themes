"""Remove theme files."""

from .util import get_themes_dir


def remove_theme_files(theme_names: list[str]) -> None:
    """
    Remove theme files from themes directory.

    Args:
        theme_names: List of theme names to remove

    """
    themes_dir = get_themes_dir()

    existing_themes = []
    non_existing_themes = []

    # Check which themes exist
    for theme in theme_names:
        theme_path = themes_dir / f"{theme}.css"
        if theme_path.exists():
            existing_themes.append(theme)
        else:
            non_existing_themes.append(theme)

    # Print non-existing themes
    if non_existing_themes:
        print("Following themes do not exist:")
        for theme in non_existing_themes:
            print(f"- {theme}")

    if not existing_themes:
        return

    # Confirm removal
    print(f"Will remove themes: {', '.join(existing_themes)}")
    response = input("Continue? (y/n): ").lower().strip()

    if response != "y":
        print("Operation cancelled")
        return

    # Remove the files
    for theme in existing_themes:
        theme_path = themes_dir / f"{theme}.css"
        theme_path.unlink()
        print(f"Removed theme: {theme}")
