class Category:
    """Категории товаров"""

    name: str
    description: str
    products: list
    num_of_categories = 0
    numb_of_products = 0

    def __init__(self, name, description, products=None):
        """Инициализация для класса Category"""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.num_of_categories += 1
        Category.numb_of_products += len(products)
