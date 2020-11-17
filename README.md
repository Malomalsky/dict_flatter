# Тестовое задание.

**Важно!** При python >= 3.8 нужно поменять

```python
from collections import MutableMapping
```

на

```python
from collections.abc import MutableMapping
```

В основе применения [функции](https://github.com/Malomalsky/dict_flatter/blob/master/function.py) лежит идея рекурсивного обхода элементов словаря.
Если значение соответсвует протоколу словаря - алгоритм углубляется дальше.
Тесты прилагаются.
