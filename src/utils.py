import json
import random


def get_file(paste_file):
    """Функция принимает файл формата .json и возвращает его списком python формата"""
    with open(paste_file) as file:
        products = json.load(file)
        return products


def get_product():
    """Функция рандомно возвращает словарь элементов из списка, для объектов класса Product"""
    products = (get_category()['products'])
    all_products = []
    for product in products:
        all_products.append(product)
    return random.choice(all_products)


def get_category():
    """Функция рандомно возвращает словарь элементов из списка, для объектов класса Category"""
    products = get_file('products.json')
    all_products = []
    for product in products:
        all_products.append(product)
    return random.choice(all_products)
