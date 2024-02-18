import json


def get_object_category(any_file):
    """Функция принимает файл формата .json и возвращает словарь объектов для класса Category"""
    with open(any_file) as file:
        products = json.load(file)
        for product in products:
            return product


def get_object_product():
    """Функция возвращает словарь объектов для класса Product"""
    products = get_object_category('products.json')['products']
    for product in products:
        return product


class Category:
    """Класс Category содержит название, описание и товары"""

    # список всех категорий
    all_category = get_object_product()
    # список уникальных продуктов
    unique_products = []

    def __init__(self, name=str, description=str, products=list):
        self.name = name
        self.description = description
        self.products = products


class Product:
    """Класс содержит название, описание, цену и количество товара, в наличии"""

    def __init__(self, name=str, description=str, price=float, quantity=int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


x = Category(get_object_category('products.json')['name'], get_object_category('products.json')['description'],
             get_object_category('products.json')['products'])

print(type(get_object_category('products.json')))
