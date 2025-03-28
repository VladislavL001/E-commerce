from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.description}, {self.price}, {self.quantity})" # noqa


class Product(BaseProduct, PrintMixin):
    """Товары"""

    products_list: list = []

    def __init__(self, name, description, price, quantity) -> None:
        """Инициализация для класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(self)
        super().__init__()

    @property
    def price(self) -> None:
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для установки цены с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if value < self.__price:
                check = input("Вы снижаете цену товара. Подтвердите выбор (Y/N)")
                if str(check).upper() == "Y":
                    self.__price = value

    @classmethod
    def new_product(cls, product_dict):
        name = product_dict.get("name")
        description = product_dict.get("description")
        price = product_dict.get("price")
        quantity = product_dict.get("quantity")

        for product in Product.products_list:
            if name == product.name:
                product.quantity += quantity
                product.__price = max(product.__price, price)
                return product

        return cls(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}: {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) == type(self): # noqa
            return f"{self.__price * self.quantity + other.__price * other.quantity} руб."
        raise TypeError


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
