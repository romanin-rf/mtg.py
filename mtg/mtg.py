import os
import re
from . import mtgdata
from PIL import ImageDraw, ImageFont, Image
from typing import Union, Optional, Any

# Класс исключений
class NotAHEXColour(Exception):
    def __init__(self, *args, **kwargs) -> None:
        """Calls if the `str` is not a `hex-colour`"""
        if len(args) != 0:
            self.msg = " ".join(args)
        else:
            if "colour" in kwargs.keys():
                self.msg = "This '%s' is not a hex-colour" % kwargs["colour"]
            else:
                self.msg = "Not a hex-colour"
    
    def __str__(self) -> str:
        return self.msg

class NotAColour(Exception):
    def __init__(self, *args, **kwargs) -> None:
        """Calls if the `str` is not a `colour`"""
        if len(args) != 0:
            self.msg = " ".join(args)
        else:
            if "colour" in kwargs.keys():
                self.msg = "This %s is not a colour" % kwargs["colour"]
            else:
                self.msg = "Not a colour"
    
    def __str__(self) -> str:
        return self.msg

# Классы
class Settings:
    def __init__(
        self,
        max_lines: int=4,
        std_xy: tuple[float, float]=(20.0, 50.0),
        font_size: int=71,
        spacing: int=100,
        dpath_table: Optional[str]=None,
        dpath_font: Optional[str]=None
    ) -> None:
        self.MaxLines: int = max_lines
        self.StandartXY: tuple[float, float] = std_xy
        self.FontSize: int = font_size
        self.Spacing: int = spacing
        self.DefultsTablePath = mtgdata.default_table_path if (dpath_table is None) else os.path.abspath(dpath_table)
        self.DefultsFontPath = mtgdata.default_font_path if (dpath_font is None) else os.path.abspath(dpath_font)

class ColoursRGBA:
    def __init__(self) -> None:
        self.colours: dict[str, tuple[int, int, int, int]] = {
            "white": (255, 255, 255, 255),
            "black": (0, 0, 0, 255),
            "red": (255, 0, 0, 255),
            "green": (0, 255, 0, 255),
            "blue": (0, 0, 255, 255),
            "yellow": (255, 247, 0, 255),
            "orange": (255, 153, 0, 255),
            "pink": (255, 0, 153, 255),
            "purple": (174, 0, 255, 255),
            "cyan": (0, 255, 238, 255),
            "gold": (255, 213, 0, 255),
            "marine": (0, 255, 179, 255),
            "brown": (125, 75, 0, 255)
        }
    
    def is_hexcolour(self, value: str) -> tuple[bool, Union[tuple[int, int, int, int], None]]:
        if value.startswith("#"):
            value = value[1:]
        if (len(value) == 6) or (len(value) == 8):
            cl = [int(i, 16) for i in re.findall(r'..', value)]
            for i in cl:
                if not((i <= 255) and (i >= 0)):
                    return False, None
            if len(cl) != 4:
                cl.append(255)
            return True, tuple(cl)
        else:
            return False, None
    
    def is_colour(self, value: tuple[int, int, int, int]) -> tuple[bool, Union[tuple[int, int, int, int], None]]:
        for i in value:
            if not((i <= 255) and (i >= 0)):
                return False, None
        return True, value
    
    def get_colours(self, full_info: bool=True) -> Union[dict[str, tuple[int, int, int, int]], list[str]]:
        return (self.colours) if (full_info) else (list(self.colours.keys()))
    
    def add_colour(self, name: str, value: tuple[int, int, int, int]) -> None:
        if self.is_colour(value)[0]:
            self.colours[name] = value
        else:
            raise NotAColour(colour=value)

    def add_colours(self, data: dict[str, tuple[int, int, int, int]]) -> None:
        for i in data.items():
            self.add_colour(i[0], i[1])
    
    def add_hexcolour(self, name: str, value: str) -> None:
        t = self.is_hexcolour(value)
        if t[0]:
            self.colours[name] = t[1]
        else:
            raise NotAHEXColour(colour=value)
    
    def add_hexcolours(self, data: dict[str, str]) -> None:
        for i in data.items():
            self.add_hexcolour(i[0], i[1])

class ColourRGBA:
    def __init__(self, d: Union[str, tuple], *, colours: Optional[ColoursRGBA]=None) -> None:
        colours = colours or ColoursRGBA()
        if isinstance(d, str):
            try:
                self.colour: tuple[int, int, int, int] = colours.colours[d]
            except:
                self.colour: tuple[int, int, int, int] = colours.colours["black"]
        elif isinstance(d, tuple):
            self.colour: tuple[int, int, int, int] = d
        else:
            self.colour: tuple[int, int, int, int] = colours.colours["black"]

def spliterator(
    text: str,
    img: Image.Image,
    font: ImageFont.ImageFont,
    settings: Settings
) -> list[str]:
    lt, idx = [], 0
    x_size = img.size[0] - (settings.StandartXY[0] * 2)
    for i in text:
        if len(lt) == 0:
            lt.append(i)
        else:
            if font.getsize(lt[idx] + i)[0] > x_size:
                idx += 1
                lt.append(i)
            else:
                lt[idx] += i

    if len(lt) > settings.MaxLines:
        return lt[:settings.MaxLines]
    else:
        return lt

def replaces(text: str, d: dict[str, str]) -> str:
    for o, n in list(d.items()):
        text = text.replace(o, n)
    return text

def handler_text(
    text: str,
    img: Image.Image,
    font: ImageFont.ImageFont,
    settings: Settings
) -> str:
    if "\n" in text:
        text = text.replace("\n", " ")
    x_size = img.size[0] - (settings.StandartXY[0] * 2)
    if not(font.getsize(text) <= x_size):
        new_text = ""
        for i in text:
            if font.getsize(new_text + i) >= x_size:
                return new_text
            else:
                new_text += i
    return text

def get_xy(
    text: str,
    line: int,
    img: Image.Image,
    font: ImageFont.ImageFont,
    settings: Settings
) -> tuple[float, float]:
    x, y = settings.StandartXY
    x += ((float(img.size[0]) - x * 2) - (font.getsize(text)[0])) / 2
    y += settings.Spacing * line
    return (x, y)

def exind(d: Union[list, tuple, dict], index: Any) -> Union[Any, None]:
    try:
        return d[index]
    except:
        return None

def from_dict(d: dict[int, str], settings: Settings) -> list[str]:
    l = []
    for i in range(0, settings.MaxLines):
        t = exind(d, i)
        if t is None:
            l.append(" ")
        else:
            l.append(t)
    return l

def generate_table(
    text: Union[str, list[str], dict[int, str]],
    colour: Optional[ColourRGBA]=None,
    *,
    settings: Optional[Settings]=None
) -> Image.Image:
    settings, colour = (settings or Settings()), (colour or ColourRGBA("black"))
    font, image = ImageFont.truetype(settings.DefultsFontPath, settings.FontSize), Image.open(settings.DefultsTablePath).convert("RGBA")
    new_image, image_draw = Image.new("RGBA", image.size, (0, 0, 0, 1)), ImageDraw.Draw(image)

    if isinstance(text, str):
        ltext = spliterator(text, image, font, settings)
    elif isinstance(text, list):
        ltext = [handler_text(i, image, font, settings) for i in text]
    elif isinstance(text, dict):
        ltext = [handler_text(i, image, font, settings) for i in from_dict(text, settings)]
    else:
        raise TypeError()

    for idx, i in enumerate(ltext):
        image_draw.text(
            text=i,
            xy=get_xy(i, idx, image, font, settings),
            font=font,
            align="left",
            fill=colour.colour
        )

    try:
        return Image.alpha_composite(image, new_image)
    except:
        return None

if __name__ == '__main__':
    try:
        import sys
        generate_table(sys.argv[1]).show()
    except:
        import time
        generate_table({1: "qwerty", 3: "123456789"}).show()
        time.sleep(3)
        generate_table(["1234567890", "qwerty", "/*-+=_()&^%$#@!"]).show()
        time.sleep(3)
        generate_table("qwertyuiopasdfghjklzxcvbnm,./;'[]123456789/*-=!@#$%^&").show()
