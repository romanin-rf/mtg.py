import os
from . import mtgdata
from PIL import ImageDraw, ImageFont, Image
from typing import Union, Optional, Any

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

class Colors:
    def __init__(self) -> None:
        self.colors: dict[str, tuple[int, int, int, int]] = {
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
    
    def get_colors(self, full: bool=True) -> Union[dict[str, tuple[int, int, int, int]], list[str]]:
        return (self.colors) if (full) else (list(self.colors.keys()))
    
    def add_color(self, name: str, value: tuple[int, int, int, int]) -> None:
        self.colors[name] = value

    def add_colors(self, data: dict[str, tuple[int, int, int, int]]) -> None:
        for i in tuple(data.items()):
            self.add_color(i[0], i[1])

class ColorRGBA:
    def __init__(self, d: Union[str, tuple], *, colors: Optional[Colors]=None) -> None:
        colors = colors or Colors()
        if isinstance(d, str):
            try:
                self.color: tuple[int, int, int, int] = colors.colors[d]
            except:
                self.color: tuple[int, int, int, int] = colors.colors["black"]
        elif isinstance(d, tuple):
            self.color: tuple[int, int, int, int] = d
        else:
            self.color: tuple[int, int, int, int] = colors.colors["black"]

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
    color: Optional[ColorRGBA]=None,
    *,
    settings: Optional[Settings]=None
) -> Image.Image:
    settings, color = (settings or Settings()), (color or ColorRGBA("black"))
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
            fill=color.color
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
