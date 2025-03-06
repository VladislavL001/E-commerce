import json
import os
from typing import List


from src.product import Product
from src.category import Category


def path_data() -> str:
    """Функция возвращает пусть к файлу JSON"""
    path_current_file = os.path.dirname(__file__)
    path_file = os.path.abspath(os.path.join(path_current_file, "..", "data", "products.json"))
    return path_file


def open_data_file(path: str) -> list[dict]:
    """Функция открывает файл JSON"""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_obj_from_json(data) -> list[Category]:
    """Функция создает копии классов Category & Product"""
    categories = []
    for categories_data in data:
        products = []
        for param in categories_data["products"]:
            products.append(Product(**param))
        categories_data["products"] = products
        categories.append(Category(**categories_data))

    return categories


if __name__ == "__main__":
    path_data_file = path_data()
    data_products = open_data_file(path_data_file)
    f = create_obj_from_json(data_products)
    print (f[1].name)

