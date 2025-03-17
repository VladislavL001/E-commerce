from unittest.mock import Mock

import pytest

from src.product import Product


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

    mock_input = mocker.patch("builtins.input", return_value="Y") # noqa
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
