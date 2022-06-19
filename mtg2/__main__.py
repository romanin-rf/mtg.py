from . import mtg2

settings = mtg2.Settings(
    max_lines=5,
    font_size=64,
    std_xy=(20., 40.0),
    spacing_xy=(20.0, 92.5)
)
colour = mtg2.ColourRGBA("ff8800")

mtg2.generate_table("TEXT", colour, settings=settings).save("j.png")