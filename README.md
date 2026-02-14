# Deckr Fonts

A font pack for the [JustMyType](https://github.com/kws/justmytype) library, providing bundled Google Fonts for the Deckr project.

## Overview

This package bundles a curated selection of Google Fonts and makes them available as a JustMyType font pack. The fonts are automatically discovered and registered when the package is installed, allowing seamless font resolution through JustMyType's unified font discovery system.

## Installation

```bash
pip install deckr-fonts
```

Or install in development mode:

```bash
pip install -e .
```

## Usage

Once installed, the font pack is automatically registered with JustMyType. No additional configuration is required:

```python
from justmytype import get_default_registry

registry = get_default_registry()

# Find and use bundled fonts
font_info = registry.find_font("Roboto", weight=400)
if font_info:
    font = font_info.load(size=16)
    print(f"Found font at: {font_info.path}")
```

### Available Font Families

This package includes the following font families:

- **Audiowide** - Display font
- **DM Sans** - Sans-serif with variable weight and optical size
- **Inter** - Sans-serif with variable weight and optical size
- **Monofett** - Display font
- **Noto Color Emoji** - Color emoji font
- **Noto Emoji** - Emoji font with variable weight
- **Roboto** - Sans-serif with variable width and weight
- **Roboto Mono** - Monospace with variable weight
- **Sixtyfour Convergence** - Pixel-style display font with multiple variable axes

### Blocking the Font Pack

If you need to disable this font pack (e.g., for testing or to use system fonts instead):

```python
from justmytype import FontRegistry

# Block via constructor
registry = FontRegistry(blocklist={"deckr-fonts"})

# Or via environment variable
# FONT_DISCOVERY_BLOCKLIST="deckr-fonts" python app.py
```

## License

### Package License

This package itself is licensed under the MIT License. See [LICENSE](LICENSE) for details.

### Font Licenses

All fonts included in this package are licensed under the **SIL Open Font License (OFL) Version 1.1**. Each font family has its own license file in the `licenses/` directory.

#### Font Attribution

- **Audiowide**: Copyright (c) 2012, Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Names "Audiowide"
- **DM Sans**: Copyright 2014 The DM Sans Project Authors (https://github.com/googlefonts/dm-fonts)
- **Inter**: Copyright 2020 The Inter Project Authors (https://github.com/rsms/inter)
- **Monofett**: Copyright 2010 The Monofett Project Authors (https://github.com/googlefonts/monofett), with Reserved Font Name Monofett.
- **Noto Color Emoji**: Copyright 2021 Google Inc. All Rights Reserved.
- **Noto Emoji**: Copyright 2013 Google LLC
- **Roboto**: Copyright 2011 The Roboto Project Authors (https://github.com/googlefonts/roboto-classic)
- **Roboto Mono**: Copyright 2015 The Roboto Mono Project Authors (https://github.com/googlefonts/robotomono)
- **Sixtyfour Convergence**: Copyright 2021 The Sixtyfour Project Authors (https://github.com/jenskutilek/homecomputer-fonts)

#### SIL Open Font License

The SIL Open Font License (OFL) allows the fonts to be:
- Used, studied, modified, and redistributed freely
- Bundled, embedded, redistributed, and/or sold with any software
- Used in commercial products

The fonts cannot be sold by themselves, and derivative works must also be released under the OFL.

Full license text is available in each font's `licenses/{fontname}/OFL.txt` file, and online at https://openfontlicense.org

## Development

### Project Structure

```
deckr_fonts/
├── src/
│   └── deckr_fonts/
│       ├── __init__.py      # Entry point factory
│       └── pack.py          # FontPack implementation
├── fonts/                   # Font files
├── licenses/                # Individual font license files
├── pyproject.toml          # PEP 621 project configuration
└── README.md                # This file
```

### Building

This package uses Poetry for building:

```bash
poetry build
```

## Requirements

- Python >= 3.10
- justmytype >= 0.3.0

## Related Projects

- [JustMyType](https://github.com/kws/justmytype) - Cross-platform font discovery library
- [Google Fonts](https://fonts.google.com/) - Source of bundled fonts

