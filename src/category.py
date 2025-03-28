from src.baseclass import baseclass
from src.product import Product


class Category(baseclass):
    """Категории товаров"""

    num_of_categories = 0
    numb_of_products = 0

    def __init__(self, name, description, products=None) -> None:
        """Инициализация для класса Category"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.num_of_categories += 1
        Category.numb_of_products += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.numb_of_products += 1
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    @property
    def products(self) -> str:
        """Возвращает список товаров"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def summ_products_category(self):
        summ = 0
        for product in self.__products:
            summ += product.quantity
        return summ

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.summ_products_category} шт."
