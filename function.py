from collections import MutableMapping  # from collection.abc если python >= 3.8


def flatten(dct, pkey='', sep='.') -> dict:
    """
    Возвращает сглаженный список.

    Аргументы:\n
        dct (MutableMapping): Входной словарь
        pkey (str): Родительский ключ, дефолт - пустой для корректной работы
        sep (str): Разделитель. ('.' по дефолту)

    Результат:\n
        dict: Сглаженный словарь
        TypeError: Если на вход функции передан не словарь.
    """
    if isinstance(dct, MutableMapping):
        pairs = []
        for key, value in dct.items():
            new_key = pkey + sep + key if pkey else key
            if isinstance(value, MutableMapping):
                pairs.extend(flatten(value, pkey=new_key).items())
            else:
                pairs.append((new_key, value))
        return dict(pairs)
    else:
        raise TypeError('Неверный формат словаря.')
