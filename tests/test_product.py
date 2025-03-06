import pytest
from tests.conftest import product_1, product_2, product_3


def test_valid_product_1(product_1) -> None:
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180_000.0
    assert product_1.quantity == 5


def test_valid_product_2(product_2) -> None:
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210_000.0
    assert product_2.quantity == 8


def test_valid_product_3(product_3) -> None:
    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31_000.0
    assert product_3.quantity == 14
