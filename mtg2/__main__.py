from . import mtg2

settings = mtg2.Settings(
    max_lines=5,
    font_size=64,
    std_xy=(20., 40.0),
    spacing_xy=(20.0, 92.5)
)

mtg2.generate_table("Hello, world! This testing is new settings! qwertyuiopasdfghjklzxcvbnm йцукенгшщзхъфывапролджэячсмитьбю 1234567890 +-*/|\\", settings=settings).show()