import unittest

from src.order import Order
from src.product import Product


class TestOrder(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый продукт с описанием
        self.product = Product(name="Телефон", price=20000, quantity=10, description="Смартфон с хорошей камерой")
        self.buy_count = 2
        self.order = Order(self.product, self.buy_count)

    def test_order_creation(self):
        # Проверка, что объект Order создан с правильными атрибутами
        self.assertEqual(self.order.product.name, "Телефон")
        self.assertEqual(self.order.product.description, "Смартфон с хорошей камерой")
        self.assertEqual(self.order.buy_count, self.buy_count)
        self.assertEqual(self.order.total_amount, 20000)

    def test_quantity_reduction(self):
        # Проверка уменьшения количества товара
        self.assertEqual(self.product.quantity, 8)  # 10 - 2 = 8

    def test_order_str(self):
        # Проверка правильного вывода строки
        expected_output = "Куплено: Телефон, кол-во: 2 шт., общая сумма покупки 20000 руб."
        self.assertEqual(str(self.order), expected_output)
