## mtg2.ColourRGBA
### Описание
На самом деле работа данного класса проста до безобразия. Для него требуеться:
- ```python 
  mtg2.ColoursRGBA(colour: str | tuple[int, int, int, int], colours: Optional[ColorsRGBA]=None)
  ```
    - Если переданое в `colour` значение - являеться **str**
        - то оно должно являвлять **hex-цветом** или **индексом к словарь** в классе [mtg2.ColorsRGBA](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md)
    - Если переданое в `colour` значение - являеться **tuple[int, int, int, int]**
        - то все значения **int** в переданом **tuple**, должны соответвовать условию:
            - ```python
              (int >= 0) and (int <= 255)
              ```
    - Перередовать в `colours`, нужно класс [mtg2.ColorsRGBA()](https://github.com/romanin-rf/mtg.py/blob/main/tutorials/mtg2/ColoursRGBA.md), ***но не обязательно***

### Пример
```python
>>> import mtg2
>>> mtg2.ColourRGBA("black")
ColourRGBA(0, 0, 0, 255)
>>> mtg2.ColourRGBA("fff")
ColourRGBA(255, 255, 255, 255)
>>> mtg2.ColourRGBA("f0f")
ColourRGBA(255, 0, 255, 255)
>>> mtg2.ColourRGBA("00f0")
ColourRGBA(0, 0, 255, 0)
>>> mtg2.ColourRGBA("#00ff00ff") # Также можно с #
ColourRGBA(0, 255, 0, 255)
```
