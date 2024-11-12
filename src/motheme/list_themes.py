"""List available themes."""

from .util import get_themes_dir


def list_themes() -> None:
    """List available themes."""
    themes_dir = get_themes_dir()
    if themes_dir.exists():
        themes = [theme.stem for theme in themes_dir.glob("*.css")]
        print("Available Themes:")
        for theme in themes:
            print(f"- {theme}")
    else:
        print("No themes downloaded. Run 'mtheme update' to download themes.")
