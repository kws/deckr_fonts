from justmytype import FontRegistry

from deckr_fonts.font_assets import inter

registry = FontRegistry()
font = registry.find_font(family="Inter", weight=400)
print(font)

asset = inter.regular
print(asset)

