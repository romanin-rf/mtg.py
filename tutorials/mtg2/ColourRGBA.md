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
