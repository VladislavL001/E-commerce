import pytest

from tests.conftest import category_1, product_1, product_2, product_3


def test_valid_category_1(category_1, product_1, product_2, product_3) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.products == (
        "Название продукта: Samsung Galaxy S23 Ultra руб. Остаток: 5 шт.\n"
        "Название продукта: Iphone 15 руб. Остаток: 8 шт.\n"
        "Название продукта: Xiaomi Redmi Note 11 руб. Остаток: 14 шт.\n"
    )

    assert category_1.num_of_categories == 1
    assert category_1.numb_of_products == 3
