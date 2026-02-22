from justmytype.font_catalog import FontCatalog, FontFamily
from justmytype.types import FontInfo

audiowide: FontFamily
dm_sans: FontFamily
inter: FontFamily
monofett: FontFamily
noto_color_emoji: FontFamily
noto_emoji: FontFamily
roboto: FontFamily
roboto_mono: FontFamily
sixtyfour_convergence: FontFamily
all_assets: tuple[FontInfo, ...]
by_postscript: dict[str, FontInfo]
def find(*, family: str, style: str | None = ..., weight: int | None = ..., postscript_name: str | None = ...) -> FontInfo | None: ...
def list_families() -> tuple[str, ...]: ...
