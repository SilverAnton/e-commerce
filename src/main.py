from src.category import Category
from src.product import Product
from src.utils import get_object_product, get_object_category


def main_foo(paste_class):
    """Главная функция печатает экземпляры классов и их атрибуты, на выбор из классов Product и Category"""
    if paste_class is Category:
        category = get_object_category('products.json')
        object_category = Category(category['name'], category['description'], category['products'])
        print(object_category.name)
        print(object_category.description)
        print(object_category.products)
        print(object_category.category_count)
        print(object_category.unique_products_count)
    elif paste_class is Product:
        product = get_object_product()
        object_product = Product(product['name'], product['description'], product['price'], product['quantity'])
        print(object_product.name)
        print(object_product.description)
        print(object_product.price)
        print(object_product.quantity_in_stock)
    else:
        print('...ой...')


main_foo(Category)
print()
main_foo(Product)
print()
main_foo(get_object_product())