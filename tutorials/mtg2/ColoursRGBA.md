## mtg2.ColoursRGBA()
### Описание
Класс [mtg2.ColoursRGBA](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md), нечего не принимает. Сделан для конвертации данных из под класса [mtg2.ColourRGBA](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColourRGBA.md).

### Пример
```python
>>> import mtg2
>>> mtg2.ColoursRGBA()
ColoursRGBA('white', 'black', 'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple', 'cyan', 'gold', 'marine', 'brown')
>>> mtg2.ColoursRGBA()["black"]
(0, 0, 0, 255)
```

### Функции
- [mtg2.ColoursRGBA.is_rgba](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md#mtg2coloursrgbais_rgba)
- [mtg2.ColoursRGBA.hex_to_rgba](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md#mtg2coloursrgbahex_to_rgba)
- [mtg2.ColoursRGBA.get_colour_type](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md#mtg2coloursrgbaget_colour_type)
- [mtg2.ColoursRGBA.get_colour](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md#mtg2coloursrgbaget_colour)
- [mtg2.ColoursRGBA.set_colour]()
- [mtg2.ColoursRGBA.set_colours]()

<hr>

## mtg2.ColoursRGBA().is_rgba
### Описание
Функция примичает `colour` в виде ***tuple[int, int, int, int]*** и проверяет являеться ли он `rgba-цветом`, и возвращает ***bool***.
```python
mtg2.ColoursRGBA.is_rgba(colour: tuple[int, int, int, int]) -> bool
```
### Пример
```python
>>> import mtg2
>>> mtg2.ColoursRGBA().is_rgba((0, 255, 183, 185))
True
>>> mtg2.ColoursRGBA().is_rgba((256, 0, 128, 255))
False
```
## mtg2.ColoursRGBA().hex_to_rgba
### Описание
Функция примичает `colour` в виде ***str*** и конвертирует в `hex-цвет`, возращает `rgba-цвет` в виде ***tuple[int, int, int, int]***, в противном случае ***None***.
```python
mtg2.ColoursRGBA.hex_to_rgba(colour: str) -> tuple[int, int, int, int] | None:
```
### Пример
```python
>>> import mtg2
>>> mtg2.ColoursRGBA().hex_to_rgba("#ff0088ff")
(255, 0, 136, 255)
>>> mtg2.ColoursRGBA().hex_to_rgba("f8f")
(255, 136, 255, 255)
>>> mtg2.ColoursRGBA().hex_to_rgba("ff0ff")
None
```
## mtg2.ColoursRGBA().get_colour_type
### Описание
Функция принимает `colour` в виде ***str*** или ***tuple[int, int, int, int]*** и возвращает `тип цвета` в виде `str`:
- 'rgba-colour'
    - это тип цвета в виде ***tuple[int, int, int, int]***
- 'hex-colour'
    - это тип цвета в виде ***str*** ([пример выше](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md#пример-2))
- 'name-colour'
    - это тип цвета, являеться `name` в классе [mtg2.ColoursRGBA](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md#пример)

<br>

В противном случае выводит ***None***.
```python
mtg2.ColoursRGBA.get_colour_type(colour: str | tuple[int, int, int, int]) -> Literal['rgba-colour', 'hex-colour', 'name-colour'] | None
```
### Пример
```python
>>> import mtg2
>>> mtg2.ColoursRGBA().get_colour_type("ff0088")
'hex-colour'
>>> mtg2.ColoursRGBA().get_colour_type("black")
'name-colour'
>>> mtg2.ColoursRGBA().get_colour_type((255, 55, 0, 78))
'rgba-colour'
>>> mtg2.ColoursRGBA().get_colour_type("f80f1")
None
```
## mtg2.ColoursRGBA().get_colour
### Описание
Функция принимает `colour` в виде ***str*** или ***tuple[int, int, int, int]*** и конвертирует `hex-цвет` если нужно, возвращает `rgba-цвет` в виде ***tuple[int, int, int, int]***, в противном случае возвращает ***None***. *Эта функция может служить проверкой данных на то являються ли они цветом.*
```python
mtg2.ColoursRGBA().get_colour(colour: str | tuple[int, int, int, int]) -> tuple[int, int, int, int] | None
```
### Пример
```python
>>> import mtg2
>>> mtg2.ColoursRGBA().get_colour("black")
(0, 0, 0, 255)
>>> mtg2.ColoursRGBA().get_colour("fff")
(255, 255, 255, 255)
>>> mtg2.ColoursRGBA().get_colour((255, 99, 10, 123))
(255, 99, 10, 123)
>>> mtg2.ColoursRGBA().get_colour((255, 988, 10, 123))
None
```
## mtg2.ColoursRGBA().set_colour
### Описание
Функция принимает `name` и `colour`, ... , в пртивном случае вызывает исключение ***NotAColourError***.
```python
mtg2.ColoursRGBA().set_colour(name: str, colour: str | tuple[int, int, int, int]) -> None
```
### Пример
```python
>>> import mtg2
>>> mtg2.ColoursRGBA().set_colour("kek", "f80122")
None
>>> mtg2.ColoursRGBA().set_colour("kek", "00000000000")
NotAColourError: ...
```
## mtg2.ColoursRGBA().set_colours
### Описание
Функция принимает `name` и `data`, ... , в пртивном случае вызывает исключение ***NotAColourError***.
```python
mtg2.ColoursRGBA().set_colours(name: str, data: dict[str, str | tuple[int, int, int, int]]) -> None
```
### Пример
```python
# Я устал писать эти примеры, описывать каждое гавно для кого-то хотя по факту этим гавно буду пользовать только я и пару людей, НЕНАВИЖУ СВОЙ ПЕРФЕКЦИОНИЗМ
```
