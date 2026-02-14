"""Unit tests for font discovery via JustMyType."""

from __future__ import annotations

from importlib.metadata import entry_points

import pytest
from justmytype import FontRegistry


class TestEntryPointRegistration:
    """Test that the deckr-fonts entry point is properly registered."""

    def test_entry_point_registered(self) -> None:
        """Test that deckr-fonts entry point is registered."""
        eps = entry_points(group="justmytype.packs")
        font_packs = [ep.name for ep in eps]
        assert (
            "deckr-fonts" in font_packs
        ), "deckr-fonts entry point should be registered"

    def test_entry_point_loadable(self) -> None:
        """Test that the entry point can be loaded and returns a FontPack."""
        eps = entry_points(group="justmytype.packs")
        deckr_ep = next((ep for ep in eps if ep.name == "deckr-fonts"), None)
        assert deckr_ep is not None, "deckr-fonts entry point should exist"

        # Load the entry point
        font_pack = deckr_ep.load()()
        assert font_pack is not None, "Entry point should return a FontPack instance"
        assert (
            font_pack.get_name() == "deckr-fonts"
        ), "Font pack should have correct name"


class TestFontDiscovery:
    """Test font discovery functionality."""

    @pytest.fixture
    def registry(self) -> FontRegistry:
        """Create a FontRegistry instance for testing."""
        registry = FontRegistry()
        registry.discover()
        return registry

    def test_discovery_finds_fonts(self, registry: FontRegistry) -> None:
        """Test that font discovery finds fonts."""
        families = list(registry.list_families())
        assert len(families) > 0, "Should discover at least one font family"

    def test_expected_font_families_present(self, registry: FontRegistry) -> None:
        """Test that expected font families are discovered."""
        families = set(registry.list_families())
        expected_families = {
            "Roboto",
            "Inter",
            "DM Sans",
            "Roboto Mono",
            "Audiowide",
            "Monofett",
        }
        for family in expected_families:
            assert (
                family in families
            ), f"Expected font family '{family}' should be discovered"


class TestFontListing:
    """Test font listing functionality using 0.2.0 features."""

    @pytest.fixture
    def registry(self) -> FontRegistry:
        """Create a FontRegistry instance for testing."""
        registry = FontRegistry()
        registry.discover()
        return registry

    def test_list_families_returns_iterable(self, registry: FontRegistry) -> None:
        """Test that list_families() returns an iterable."""
        families = registry.list_families()
        assert hasattr(
            families, "__iter__"
        ), "list_families() should return an iterable"
        family_list = list(families)
        assert isinstance(family_list, list), "Should be able to convert to list"

    def test_list_families_returns_strings(self, registry: FontRegistry) -> None:
        """Test that list_families() returns string family names."""
        families = list(registry.list_families())
        assert len(families) > 0, "Should have at least one family"
        for family in families:
            assert isinstance(
                family, str
            ), f"Family name should be a string, got {type(family)}"
            assert len(family) > 0, "Family name should not be empty"

    def test_list_families_sorted(self, registry: FontRegistry) -> None:
        """Test that we can get sorted family names."""
        families = list(registry.list_families())
        sorted_families = sorted(families)
        assert sorted_families == sorted(
            set(families)
        ), "Should be able to sort families"


class TestFontResolution:
    """Test font resolution functionality."""

    @pytest.fixture
    def registry(self) -> FontRegistry:
        """Create a FontRegistry instance for testing."""
        registry = FontRegistry()
        registry.discover()
        return registry

    @pytest.mark.parametrize(
        ("family", "weight", "style"),
        [
            ("Roboto", 400, "normal"),
            ("Roboto", 700, "normal"),
            ("Inter", 400, "normal"),
            ("Inter", 400, "italic"),
            ("DM Sans", 500, "normal"),
            ("Roboto Mono", 400, "normal"),
            ("Audiowide", None, "normal"),
            ("Monofett", None, "normal"),
        ],
    )
    def test_find_font(
        self,
        registry: FontRegistry,
        family: str,
        weight: int | None,
        style: str,
    ) -> None:
        """Test finding specific fonts with various weights and styles."""
        font_info = registry.find_font(family, weight=weight, style=style)
        assert (
            font_info is not None
        ), f"Should find {family} (weight={weight}, style={style})"
        assert font_info.family == family, "Font info should have correct family name"
        assert font_info.path.exists(), f"Font file should exist at {font_info.path}"

        if weight is not None:
            # Variable fonts may have different weight values, so just check it's set
            assert (
                font_info.weight is not None
            ), "Font info should have weight when specified"

    def test_find_font_nonexistent(self, registry: FontRegistry) -> None:
        """Test that finding a nonexistent font returns None."""
        font_info = registry.find_font("NonexistentFont", weight=400, style="normal")
        assert font_info is None, "Should return None for nonexistent font"


class TestFontSources:
    """Test that fonts are from the deckr-fonts pack."""

    @pytest.fixture
    def registry(self) -> FontRegistry:
        """Create a FontRegistry instance for testing."""
        registry = FontRegistry()
        registry.discover()
        return registry

    def test_fonts_from_deckr_fonts_pack(self, registry: FontRegistry) -> None:
        """Test that discovered fonts are from the deckr-fonts pack."""
        families = list(registry.list_families())
        deckr_fonts_found = []

        for family in families:
            font_info = registry.find_font(family)
            if font_info:
                # Check if path is in our fonts directory
                path_str = str(font_info.path)
                if "deckr_fonts" in path_str or "fonts" in path_str:
                    deckr_fonts_found.append(family)

        assert len(deckr_fonts_found) > 0, "Should find fonts from deckr-fonts pack"
        # Verify some expected fonts are from our pack
        expected_in_pack = {"Roboto", "Inter", "DM Sans", "Audiowide", "Monofett"}
        found_expected = set(deckr_fonts_found) & expected_in_pack
        assert (
            len(found_expected) > 0
        ), f"Should find at least some expected fonts: {found_expected}"
