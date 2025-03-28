import unittest
from unittest.mock import Mock

import pytest

from src.product import BaseProduct, Product


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


def test_valid_new_product(capsys: pytest.CaptureFixture, mocker: Mock) -> None:
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180_000.0
    assert new_product.quantity == 10

    mock_input = mocker.patch("builtins.input", return_value="Y")  # noqa
    new_product.price = 800
    assert new_product.price == 800

    new_product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    new_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_valid_product_add(product_1, product_2, product_3):
    assert product_1 + product_2 == "2580000.0 руб."
    assert product_1 + product_3 == "1334000.0 руб."


def test_valid_product_str(product_1, product_2, product_3) -> None:
    assert str(product_1) == "Samsung Galaxy S23 Ultra: 180000.0 руб. Остаток: 5 шт."
    assert str(product_2) == "Iphone 15: 210000.0 руб. Остаток: 8 шт."
    assert str(product_3) == "Xiaomi Redmi Note 11: 31000.0 руб. Остаток: 14 шт."


def test_valid_smartphone(smartphone1, smartphone2, smartphone3) -> None:
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"

    assert smartphone3.name == "Xiaomi Redmi Note 11"
    assert smartphone3.description == "1024GB, Синий"
    assert smartphone3.price == 31000.0
    assert smartphone3.quantity == 14
    assert smartphone3.efficiency == 90.3
    assert smartphone3.model == "Note 11"
    assert smartphone3.memory == 1024
    assert smartphone3.color == "Синий"


def test_valid_lawn_grass(grass1, grass2) -> None:
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"

    assert grass2.name == "Газонная трава 2"
    assert grass2.description == "Выносливая трава"
    assert grass2.price == 450.0
    assert grass2.quantity == 15
    assert grass2.country == "США"
    assert grass2.germination_period == "5 дней"
    assert grass2.color == "Темно-зеленый"


def test_add_products(smartphone1, smartphone2, grass1, grass2):
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == "2580000.0 руб."

    grass_sum = grass1 + grass2
    assert grass_sum == "16750.0 руб."

    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_valid_base_product() -> None:
    class ConcreteProduct(BaseProduct):
        @classmethod
        def new_product(cls, name, price):
            return {"name": name, "price": price}

    # Тестовый класс для проверки BaseProduct
    class TestBaseProduct(unittest.TestCase):
        def test_new_product(self):
            product = ConcreteProduct.new_product("Laptop", 1000)
            self.assertEqual(product, {"name": "Laptop", "price": 1000})
