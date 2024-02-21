import json


def get_object_category(any_file):
    """Функция принимает файл формата .json и возвращает словарь для создания экземпляров класса Category"""
    with open(any_file) as file:
        products = json.load(file)
        for product in products:
            return product


def get_object_product():
    """Функция возвращает словарь объектов для класса Product"""
    products = get_object_category('products.json')['products']
    for product in products:
        return product
