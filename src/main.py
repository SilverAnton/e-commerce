from src.category import Category
from src.product import Product
from src.utils import get_category, get_product


def main_foo(paste_class):
    """Главная функция возвращает объект класса, в зависимости от выбранного класса в качестве аргумента"""
    object_product = Product(get_product()['name'], get_product()['description'], get_product()['price'],
                             get_product()['quantity'])
    object_category = Category(get_category()['name'], get_category()['description'], get_category()['products'])
    if paste_class == Product:
        return object_product
    elif paste_class == Category:
        return object_category


print(main_foo(Category).products)
print(main_foo(Product).description)
