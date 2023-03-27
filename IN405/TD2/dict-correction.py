#!/usr/bin/python3

import unittest

def merge_integer(dict_a, dict_b):
    """
    le contenu de la liste `dict_b` est ajouté à `dict_a`, si la clé existe dans
    `dict_a`, on considère que les valeurs dans `dict_a` et `dict_b` sont des
    entiers, et on remplace la valeur de `dict_a` par la moyenne des deux
    """
    for key, val in dict_b.items():
        dict_a[key] = val if key not in dict_a else int((dict_a[key] + val) / 2)

def merge_list(dict_a, dict_b):
    """
    le contenu de la liste `dict_b` est ajouté à `dict_a`, si la clé existe dans
    `dict_a`, on remplace par une liste contenant les deux valeurs
    """
    for key, val in dict_b.items():
        dict_a[key] = val if key not in dict_a else [dict_a[key], val]

def merge_smart_list(dict_a, dict_b):
    """
    le contenu de la liste `dict_b` est ajouté à `dict_a`, si la clé existe dans
    `dict_a`, on remplace par une liste contenant les deux valeurs, mais si la
    valeur de `dict_a` est déjà une liste, on ajoute la valeur de `dict_b` à
    la liste
    """
    for key, val in dict_b.items():
        if key in dict_a:
            if isinstance(dict_a[key], list):
                dict_a[key].append(val)
            else:
                dict_a[key] = [dict_a[key], val]
        else:
            dict_a[key] = val

def merge_strings(dict_a, dict_b):
    """
    le contenu de la liste `dict_b` est ajouté à `dict_a`, si la clé existe dans
    `dict_a`, on considère que les valeurs dans `dict_a` et `dict_b` sont des
    chaînes de caractères, et on remplace la valeur de `dict_a` par la
    concaténation des deux
    """
    for key, val in dict_b.items():
        dict_a[key] = val if key not in dict_a else dict_a[key] + val

class TestMergeInteger(unittest.TestCase):
    def test_null_merge(self):
        A = {}
        B = {}
        merge_integer(A, B)
        self.assertDictEqual(A, {})
        B = {'a': 42}
        merge_integer(A, B)
        self.assertDictEqual(A, {'a': 42})
        B = {}
        merge_integer(A, B)
        self.assertDictEqual(A, {'a': 42})
    def test_simple_merge(self):
        A = {'a': 42}
        B = {'b': 17}
        merge_integer(A, B)
        self.assertDictEqual(A, {'a': 42, 'b': 17})
    def test_not_unique_merge(self):
        A = {'a': 42}
        B = {'b': 17, 'c': 13}
        merge_integer(A, B)
        self.assertDictEqual(A, {'a': 42, 'b': 17, 'c': 13})
        B = {'b': 67, 'c': 72}
        merge_integer(A, B)
        self.assertDictEqual(A, {'a': 42, 'b': 42, 'c': 42})

class TestMergeList(unittest.TestCase):
    def test_null_merge(self):
        A = {}
        B = {}
        merge_list(A, B)
        self.assertDictEqual(A, {})
        B = {'a': 42}
        merge_list(A, B)
        self.assertDictEqual(A, {'a': 42})
        B = {}
        merge_list(A, B)
        self.assertDictEqual(A, {'a': 42})
    def test_simple_merge(self):
        A = {'a': 42}
        B = {'b': 17}
        merge_list(A, B)
        self.assertDictEqual(A, {'a': 42, 'b': 17})
    def test_not_unique_merge(self):
        A = {'a': 42, 'b': 3}
        B = {'b': 17, 'c': 13}
        merge_list(A, B)
        self.assertDictEqual(A, {'a': 42, 'b': [3, 17], 'c': 13})
        B = {'b': 67, 'c': 72}
        merge_list(A, B)
        self.assertDictEqual(A, {'a': 42, 'b': [[3, 17], 67], 'c': [13, 72]})

if __name__ == '__main__':
    unittest.main()