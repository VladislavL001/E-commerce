import unittest

from src.baseclass import baseclass


class DerivedClass(baseclass):
    def __str__(self):
        return "Derived class implementation"


class TestBaseClass(unittest.TestCase):
    def test_abstract_method_implementation(self):
        obj = DerivedClass()
        self.assertEqual(str(obj), "Derived class implementation")

    def test_cannot_instantiate_baseclass(self):
        with self.assertRaises(TypeError):
            baseclass()
