from src.category import Category
from src.product import Product
from src.utils import get_category, get_product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


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


#print(obj2)


#print(len(obj1))


class New:
    """Новый класс для проверки функций, уже существующих классов"""
    pass

class PassClass(Product):
    pass

obj6 = PassClass(None, None, None, None)
obj4 = New()
#obj2_2 = main_foo(Product)
obj3 = Smartphone('телефон', 'отличный телефон', 10000.90, 10, 9800.00, 'superphone', 2024.789, 'base')
obj5 = LawnGrass('мятлик', 'мягкая газонная трава', 4000.0, 10, 'England', '2а дня на прорастание', 'зеленый изумруд')
#print(obj3)
#print(obj5.made_in)
#print(obj2 + obj3)

#obj1.add_product(obj2)
#obj1.add_product(obj2)
#print(len(obj1.products))

#obj1.add_product(obj5)
#obj1.add_product(obj2)
#print(obj1.products)
print(obj1.products_av_price)
