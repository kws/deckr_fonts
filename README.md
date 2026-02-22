<!-- This file is auto-generated. Do not edit manually. -->

# Deckr Fonts

Font pack for Deckr project - Google Fonts bundle for JustMyType

## Installation

```bash
pip install deckr-fonts
```

## Usage

**Discovery (registry):**

```python
from justmytype import FontRegistry

registry = FontRegistry()
font = registry.find_font(family="Inter", weight=400)
if font:
    path = font.path  # path to the font file
    pil_font = font.load(size=24)  # PIL ImageFont (requires Pillow)
```

**Deterministic imports (pack-specific, version-pinned):**

```python
from deckr_fonts import font_assets

# Family names depend on this pack; e.g. font_assets.inter.regular
asset = font_assets.inter.regular
path = asset.path  # path to the font file
pil_font = asset.load(size=24)  # PIL ImageFont (requires Pillow)
```

## Families

| Font | License | Full text |
|------|---------|-----------|
| ofl/audiowide | OFL-1.1 | [`fonts/ofl/audiowide/OFL.txt`](src/deckr_fonts/fonts/ofl/audiowide/OFL.txt) |
| ofl/dmsans | OFL-1.1 | [`fonts/ofl/dmsans/OFL.txt`](src/deckr_fonts/fonts/ofl/dmsans/OFL.txt) |
| ofl/inter | OFL-1.1 | [`fonts/ofl/inter/OFL.txt`](src/deckr_fonts/fonts/ofl/inter/OFL.txt) |
| ofl/monofett | OFL-1.1 | [`fonts/ofl/monofett/OFL.txt`](src/deckr_fonts/fonts/ofl/monofett/OFL.txt) |
| ofl/notocoloremoji | OFL-1.1 | [`fonts/ofl/notocoloremoji/OFL.txt`](src/deckr_fonts/fonts/ofl/notocoloremoji/OFL.txt) |
| ofl/notoemoji | OFL-1.1 | [`fonts/ofl/notoemoji/OFL.txt`](src/deckr_fonts/fonts/ofl/notoemoji/OFL.txt) |
| ofl/roboto | OFL-1.1 | [`fonts/ofl/roboto/OFL.txt`](src/deckr_fonts/fonts/ofl/roboto/OFL.txt) |
| ofl/robotomono | OFL-1.1 | [`fonts/ofl/robotomono/OFL.txt`](src/deckr_fonts/fonts/ofl/robotomono/OFL.txt) |
| ofl/sixtyfourconvergence | OFL-1.1 | [`fonts/ofl/sixtyfourconvergence/OFL.txt`](src/deckr_fonts/fonts/ofl/sixtyfourconvergence/OFL.txt) |


## Upstream

Source: https://github.com/google/fonts @ 388e257

## Development

- **Fetch:** `pack-tools fetch <pack_dir>` — downloads upstream fonts into cache.
- **Build:** `pack-tools build <pack_dir>` — copies fonts into the pack, generates `pack_manifest.json` and this README.
- **Dist:** `pip install -e .` or build the wheel from the pack directory.

README is generated during build from the same resolved license data as the manifest.