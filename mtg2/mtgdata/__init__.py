import os

default_table_path: str = os.path.abspath(
    os.path.split(__file__)[0] + os.sep + "table.png"
)
default_font_path: str = os.path.abspath(
    os.path.split(__file__)[0] + os.sep + "minecraft.ttf"
)