# mtg.py
## Описание
mtg.py - Minecraft Table Generator.<br>То есть он генерирует таблички из Minecraft c текстом.
## Пример
### Код **№1**:
```python
import mtg

mtg.generate_table("Python - Топ!", mtg.ColorRGBA("green")).show()
```
### Вывод:
![image0](https://user-images.githubusercontent.com/60302782/167923777-10238f17-092b-4b18-a554-dbdc158a678b.png)
### Код **№2**:
```python
import mtg

mtg.generate_table(["Python", "ТОП"], mtg.ColorRGBA("green")).show()
```
### Вывод:
![image1](https://user-images.githubusercontent.com/60302782/167924854-bb32a8f8-822e-4a71-a8cd-b1e7c0225395.png)
### Код **№3**:
```python
import mtg

mtg.generate_table({1: "Python", 3: "ТОП"}, mtg.ColorRGBA("green")).show()
```
### Вывод:
![tmp1](https://user-images.githubusercontent.com/60302782/167925145-af7a1c9f-928d-4f8e-9b46-8a35cfd72203.png)
## Автор
- **Роман Слабицкий**
  - [VK](https://vk.com/romanin2)
