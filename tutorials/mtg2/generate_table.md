## mtg2.generate_table
### Описание
```python
mtg2.generate_table(
    text: str | list[str] | dict[int, str],
    colour: ColourRGBA | None = None,
    settings: Settings | None = None
) -> Image | None:
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
colour = mtg2.ColourRGBA("ff8800")

mtg2.generate_table("TEXT", colour, settings=settings).show()
```
- `Вывод`

![j](https://user-images.githubusercontent.com/60302782/169685113-b398fcba-37b7-41cf-8663-fb748fefda3a.png)
