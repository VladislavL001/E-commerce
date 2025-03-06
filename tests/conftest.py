from itertools import product
from symtable import Class

from src.product import Product
from src.category import Category
import pytest


@pytest.fixture
def product_1() -> Product:
    """Продукт один"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_2() -> Product:
    """Продукт два"""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_3() -> Product:
    """Продукт три"""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_1(product_1, product_2, product_3) -> Category:
    """Категория 1 - смартфоны"""
    product1 = product_1
    product2 = product_2
    product3 = product_3
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
