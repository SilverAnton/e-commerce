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


# проверка получения объектов классов и работа с ними(раскомментируйте печать нужного метода)

obj1 = main_foo(Category)
obj2 = main_foo(Product)
products = get_product()
# print(obj1.get_products())
# print(obj2.new_objects(products).name)
# print(obj2.new_objects(products).description)
# print(obj2.new_objects(products).price)
# print(obj2.new_objects(products).quantity_in_stock)

# obj2.price = 10
# print(obj2.price)

new_object = obj2.new_objects(products)
obj1.add_product(new_object)

# print(obj1.product)
