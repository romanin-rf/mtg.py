import os
import re
try:
    from . import mtgdata
except:
    import mtgdata
from PIL import ImageDraw, ImageFont, Image
from typing import Union, Optional, Literal, Any

# Классы-исключения
class NotAColourError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        """Вызываеться, если данные не являються цветом"""
        if len(args) == 0:
            if "colour" in kwargs.keys():
                self.msg = "This '%s' is not a colour" % str(kwargs["colour"])
            else:
                self.msg = "Not a colour"
        else:
            self.msg = " ".join([str(i) for i in args])
    
    def __str__(self) -> str:
        return self.msg

# Класс настройки
class Settings:
    def __init__(
        self,
        std_xy: tuple[float, float]=(20.0, 50.0),
        font_size: int=72,
        max_lines: int=4,
        spacing_xy: tuple[float, float]=(20.0, 105.0),
        dpath_table: Optional[str]=None,
        dpath_font: Optional[str]=None
    ) -> None:
        """Класс настройки, a именно:\n\n\
        - `расположение текста` (std_xy)\n\
        - `размер текста` (font_size)\n\
        - `количество строк` (max_lines)\n\
        - `размер отступов` (spacing_xy)\n\
        - `изображение таблички` (dpath_table)\n\
        - `шрифт` (dpath_font)\
        """
        self.MaxLines: int = max_lines
        self.FontSize: int = font_size
        self.StandartXY: tuple[float, float] = std_xy
        self.Spacing: tuple[int, int] = spacing_xy
        self.DefultsTablePath = mtgdata.default_table_path if (dpath_table is None) else os.path.abspath(dpath_table)
        self.DefultsFontPath = mtgdata.default_font_path if (dpath_font is None) else os.path.abspath(dpath_font)

class ColoursRGBA:
    def __init__(self) -> None:
        """Класс для работы с `rgba-colour`\n\nИспользуеться как настройки для класса `ColorRGBA`"""
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
    
    def __repr__(self):
        return "{name}({colours})".format(name=self.__class__.__name__, colours=", ".join([("'" + i + "'") for i in self.colours.keys()]))

    def __getitem__(self, key: str) -> tuple[int, int, int, int]:
        return self.colours[key]

    def is_rgba(
        self,
        colour: tuple[int, int, int, int]
    ) -> bool:
        """Проверяет являеються ли `данные` в виде `tuple` - `rgba-colour`"""
        for i in colour:
            if not((i >= 0) and (i <= 255)):
                return False
        return True

    def hex_to_rgba(
        self,
        colour: str
    ) -> Union[tuple[int, int, int, int], None]:
        """Получает `hex-colour` в виде `str`, и возвращает `rgba-colour` в виде `tuple`, в противном случае - `None`"""
        # Срезание, если нужно
        if colour.startswith("#"):
            colour = colour[1:]
        # Проверка по длине и конвертация
        try:
            if (len(colour) == 3) or (len(colour) == 4):
                cl = [int(i, 16) for i in [(str(i)*2) for i in re.findall(r'.', colour)]]
            elif (len(colour) == 6) or (len(colour) == 8):
                cl = [int(i, 16) for i in re.findall(r'..', colour)]
            else:
                return None
        except:
            return None
        if len(cl) != 4:
            cl.append(255)
        # Проверка на правильность
        if self.is_rgba(tuple(cl)):
            return tuple(cl)

    def get_colour_type(
        self,
        colour: Union[str, tuple[int, int, int, int]]
    ) -> Union[Union[Literal['rgba-colour'], Literal['hex-colour'], Literal['name-colour']], None]:
        """Определяет тип цвета.\n\nСуществующие типы цветов: `rgba-colour`, `hex-colour`, `name-colour`"""
        if isinstance(colour, str):
            if colour in self.colours.keys():
                return "name-colour"
            if self.hex_to_rgba(colour) != None:
                return "hex-colour"
        elif isinstance(colour, tuple):
            if self.is_rgba(colour):
                return "rgba-colour"
    
    def get_colour(
        self,
        colour: Union[str, tuple[int, int, int, int]]
    ) -> Union[tuple[int, int, int, int], None]:
        """Принимает `colour`, возращает `tuple[int, int, int, int]`, в противном случае `None`"""
        colour_type = self.get_colour_type(colour)
        if colour_type == "name-colour":
            return self.colours[colour]
        elif colour_type == "rgba-colour":
            return colour
        elif colour_type == "hex-colour":
            return self.hex_to_rgba(colour)
    
    def set_colour(
        self,
        name: str,
        colour: Union[str, tuple[int, int, int, int]]
    ) -> None:
        """`Добавляет`/`Заменяет` - `colour`, при необходимости конвертирует из `hex-colour`, в противном случает вызывает `NotAColourError`"""
        colour = self.get_colour(colour)
        if colour != None:
            self.colours[name] = colour
        else:
            raise NotAColourError(colour=colour)
    
    def set_colours(self, data: dict[str, Union[str, tuple[int, int, int, int]]]) -> None:
        """Анологичен `set_colour`, только `многократный`"""
        for i in data.items():
            self.set_colour(i[0], i[1])

class ColourRGBA:
    def __init__(
        self,
        colour: Union[str, tuple[int, int, int, int]],
        colours: Optional[ColoursRGBA]=None
    ) -> None:
        """\
        Класс хранения `colour`, любого типа, при необходимости конвертирует.\
        \n\nЕсли возникнет ошибка, то `colour` по умолчанию:\
        \n- colour -> (0, 0, 0, 255)"""
        colours = colours or ColoursRGBA()
        self.colour: tuple[int, int, int, int] = colours.get_colour(colour) or colours.colours["black"]
    
    def __repr__(self):
        return "{name}({colour})".format(name=self.__class__.__name__, colour=", ".join([str(i) for i in self.colour]))

# Функции расчёта
def get_xy(
    text: str,
    idx: int,
    img: Image.Image,
    font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont],
    settings: Settings
) -> tuple[float, float]:
    text_size = font.getsize(text)
    x, y = settings.StandartXY
    x += ((img.size[0] - (settings.Spacing[0] * 2)) - text_size[0]) / 2
    y += (settings.Spacing[1] * idx)
    return x, y

def splitator(
    text: Union[str, list[str], dict[int, str]],
    img: Image.Image,
    font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont],
    settings: Settings
) -> list[str]:
    max_x = img.size[0] - (settings.Spacing[0] * 2)
    if isinstance(text, str):
        text, l, idx = text.replace("\n", " "), [], 0
        for i in text:
            if len(l) == 0:
                l.append(i)
            else:
                if font.getsize(l[idx]+i)[0] >= max_x:
                    idx += 1
                    l.append(i)
                else:
                    l[idx] += i
        return l[:settings.MaxLines]
    elif isinstance(text, list):
        l, idx = [], 0
        for i_text in text:
            if font.getsize(i_text)[0] >= max_x:
                for i in i_text:
                    if len(l) == 0:
                        l.append(i)
                    else:
                        if font.getsize(l[idx]+i)[0] >= max_x:
                            idx += 1
                            l.append(i)
                        else:
                            l[idx] += i
            else:
                idx += 1
                l.append(i_text)
        return l[:settings.MaxLines]
    elif isinstance(text, dict):
        l, idx = [" " for _ in range(settings.MaxLines)], 0
        for idx, i in tuple(text.items()):
            if (idx <= settings.MaxLines-1) and (idx >= 0):
                l[idx] = i
            else:
                return ["HandlerText", "IndexError", "idx > (max_lines-1)"]
        return l
    else:
        return ["HandlerText", "TypeError"]

# Основная функция
def generate_table(
    text: Union[str, list[str], dict[int, str]],
    colour: Optional[ColourRGBA]=None,
    settings: Optional[Settings]=None
) -> Union[Image.Image, None]:
    """Генерирует `Image.Image` из `text`, при ошибке возыращает `None`."""
    settings, colour = (settings or Settings()), (colour or ColourRGBA("black"))
    font, image = ImageFont.truetype(settings.DefultsFontPath, settings.FontSize), Image.open(settings.DefultsTablePath).convert("RGBA")
    new_image, image_draw = Image.new("RGBA", image.size, (0, 0, 0, 1)), ImageDraw.Draw(image)

    # Разделение текста на строки
    lines = splitator(text, image, font, settings)

    # Рисование текста на изображение
    try:
        for idx, i in enumerate(lines):
            image_draw.text(
                xy=get_xy(i, idx, image, font, settings),
                text=i,
                fill=colour.colour,
                font=font,
                aling="left"
            )
        # Вывод
        return Image.alpha_composite(image, new_image)
    except:
        return None