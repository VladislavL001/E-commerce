import pytest

from src.Product_iterator import ProductIterator


def test_product_iter_valid(capsys: pytest.CaptureFixture, product_1, product_2, product_3, category_1) -> None:
    iterator = ProductIterator(category_1)
    for i in iterator:
        print(i)

    captured = capsys.readouterr()
    assert (
        "Samsung Galaxy S23 Ultra: 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15: 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11: 31000.0 руб. Остаток: 14 шт.\n" in captured.out
    )
