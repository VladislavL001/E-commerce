class Product:
    """Товары"""

    products_list: list = []

    def __init__(self, name, description, price, quantity) -> None:
        """Инициализация для класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(self)

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
