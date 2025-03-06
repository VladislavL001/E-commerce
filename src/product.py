class Product:
    """Товары"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация для класса Product"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
