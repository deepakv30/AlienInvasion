"""Resolve paths to packaged game assets."""

from pathlib import Path

# Package root: alien_invasion/
PACKAGE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = PACKAGE_DIR / "images"


def image_path(filename: str) -> str:
    """Return an absolute filesystem path for an image asset."""
    return str(IMAGES_DIR / filename)
