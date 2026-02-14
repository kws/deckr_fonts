"""Font pack implementation for Deckr fonts."""

from __future__ import annotations

from pathlib import Path


class DeckrFontPack:
    """Font pack providing Deckr bundled fonts from Google Fonts."""

    def get_font_directories(self) -> list[Path]:
        """Return list of directories containing font files.

        Returns:
            List of Path objects pointing to the fonts directory.
        """
        # Resolve fonts directory relative to this package
        # Structure: src/deckr_fonts/pack.py -> fonts/
        package_dir = Path(__file__).parent.parent.parent
        fonts_dir = package_dir / "fonts"
        return [fonts_dir]

    def get_priority(self) -> int:
        """Return priority for this pack (higher = processed first, overrides lower priority).

        Standard priorities:
        - User Font Packs: 100
        - System Font Pack: 0

        Returns:
            Integer priority value (100 for bundled fonts).
        """
        return 100

    def get_name(self) -> str:
        """Return canonical name for this pack (used in blocklist).

        Returns:
            String identifier "deckr-fonts".
        """
        return "deckr-fonts"
