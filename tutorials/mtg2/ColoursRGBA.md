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
- mtg2.ColoursRGBA.hex_to_rgba
- mtg2.ColoursRGBA.get_colour_type
- mtg2.ColoursRGBA.get_colour
- mtg2.ColoursRGBA.set_colour
- mtg2.ColoursRGBA.set_colours

<hr>

## mtg2.ColoursRGBA().is_rgba
### Описание
Функция примичает `colour` в виде ***tuple[int, int, int, int]*** и проверяет являеться ли он `rgba-цветом`, и возвращает ***bool***.
```python
mtg2.ColoursRGBA().is_rgba(colour: tuple[int, int, int, int]) -> bool
```
### Пример
```python
>>> import mtg2
>>> mtg2.ColoursRGBA().is_rgba((0, 255, 183, 185))
True
>>> mtg2.ColoursRGBA().is_rgba((256, 0, 128, 255))
False
```
