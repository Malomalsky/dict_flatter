import unittest
from collections import OrderedDict
from typing import MutableMapping

from function import flatten


class TestFuncMethods(unittest.TestCase):

    def test_BuiltInDict(self): 
        """Проверяем встроенные словари"""
        dct = {"a": 5, "b": 6, "c": {"f": 9, "g": {"m": 17, "n": 3}}}
        flat_dct = {'a': 5,'b': 6,'c.f': 9,'c.g.m': 17,'c.g.n': 3}

        self.assertEqual(flatten(dct), flat_dct)

    def test_customDict(self): 
        """Проверяем кастомный объект, соответсвующий протоколу Mutable mapping"""
        dct = OrderedDict({"a": 5, "b": 6, "c": {"f": 9, "g": {"m": 17, "n": 3}}})
        flat_dct = {'a': 5,'b': 6,'c.f': 9,'c.g.m': 17,'c.g.n': 3}
        
        self.assertEqual(flatten(dct), flat_dct)


if __name__ == '__main__':
    unittest.main()
