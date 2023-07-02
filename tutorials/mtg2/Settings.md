## mtg2.Settings()
### Описание
Данный класс являеться простой настройкой для функции [mtg2.generate_table](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/generate_table.md#mtg2generate_table).
```python
settings = mtg2.Settings(
     max_lines: int=4,
     font_size: int=72,
     std_xy: tuple[float, float]=(20.0, 50.0),
     spacing_xy: tuple[float, float]=(20.0, 105.0),
     dpath_table: Optional[str]=None,
     dpath_font: Optional[str]=None
)
```
### Пример
- `main.py`
```python
import mtg2

settings = mtg2.Settings(
    max_lines=5,
    font_size=64,
    std_xy=(20., 40.0),
    spacing_xy=(20.0, 92.5)
)

image = mtg2.generate_table("Hello, world! This testing is new settings! qwertyuiopasdfghjklzxcvbnm йцукенгшщзхъфывапролджэячсмитьбю 1234567890 +-*/|\\", settings=settings)

image.show()
```
- Вывод:
![test](https://user-images.githubusercontent.com/60302782/168538884-89641bd4-723c-4f75-8a7c-1760a8c0135e.png)
