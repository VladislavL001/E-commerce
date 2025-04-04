import pytest

from src.category import Category


def test_valid_category_1(category_1, product_1, product_2, product_3) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.products == (
        "Samsung Galaxy S23 Ultra: 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15: 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11: 31000.0 руб. Остаток: 14 шт.\n"
    )

    assert category_1.num_of_categories == 2
    assert category_1.numb_of_products == 6


def test_valid_print_category(capsys: pytest.CaptureFixture, category_1) -> None:
    assert str(category_1) == "Смартфоны, количество продуктов: 27 шт."


def test_valid_add_category(smartphone1, smartphone2) -> None:
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")  # noqa

def test_error_category_class_category_empty() -> None:
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0

def test_valid_category_class_category_empty(category_1, product_1, product_2, product_3) -> None:
    assert category_1.middle_price() == 140333