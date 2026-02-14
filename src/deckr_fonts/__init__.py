"""Deckr Font Pack - Google Fonts bundle for JustMyType."""

from __future__ import annotations

from justmytype.types import FontPack

from deckr_fonts.pack import DeckrFontPack  # noqa: F401

__all__ = ["get_font_pack", "DeckrFontPack"]


def get_font_pack() -> FontPack:
    """Entry point factory for Deckr font pack.

    This function is registered as an entry point in pyproject.toml
    under the "justmytype.packs" group. It returns a FontPack instance that
    provides access to the bundled Google Fonts.

    Returns:
        DeckrFontPack instance implementing the FontPack protocol.
    """
    return DeckrFontPack()
