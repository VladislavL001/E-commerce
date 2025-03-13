from src.product import Product


class Category:
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
        self.__products.append(product)
        Category.numb_of_products += 1

    @property
    def products(self) -> str:
        """Возвращает список товаров"""
        product_str = ""
        for product in self.__products:
            product_str += f"Название продукта: {product.name} руб. Остаток: {product.quantity} шт.\n"
        return product_str
