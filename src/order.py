from src.product import Product
from src.baseclass import baseclass

class Order(baseclass):
    def __init__(self, product: Product, buy_count: int):
        self.product = product
        self.buy_count = buy_count
        self.total_amount = self.product.price
        self.product.quantity -= self.buy_count

    def __str__(self):
        return (f"Куплено: {self.product.name}, кол-во: {self.buy_count} шт., общая сумма покупки {self.total_amount} "
                f"руб.")