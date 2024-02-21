from src.utils import get_object_product, get_object_category
from src.product import Product
from src.category import Category
import pytest


@pytest.fixture
def objects_category():
    category = get_object_category('products.json')
    return Category(category['name'], category['description'], category['products'])


@pytest.fixture
def objects_product():
    product = get_object_product()
    return Product(product['name'], product['description'], product['price'], product['quantity'])


def test_init_category(objects_category):
    """Тест проверяет корректность инициализации объектов класса Category"""
    assert objects_category.name == 'Смартфоны'
    assert objects_category.description == ('Смартфоны, как средство не только коммуникации, но и получение '
                                            'дополнительных функций для удобства жизни')
    assert type(objects_category.products) is list  # в данном случае проверяем корректность инициализации типа объекта
    assert objects_category.category_count == 1
    assert objects_category.unique_products_count == 3


def test_init_product(objects_product):
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert objects_product.name == 'Samsung Galaxy C23 Ultra'
    assert objects_product.description == '256GB, Серый цвет, 200MP камера'
    assert objects_product.price == 180000.0
    assert objects_product.quantity_in_stock == 5


def test_get_object_category():
    """Тест проверяет правильность возвращенного типа объекта из функции get_object_category"""
    category = get_object_category('products.json')
    assert type(category) is dict


def test_get_object_product():
    """Тест проверяет правильность возвращенного типа объекта из функции get_object_product"""
    product = get_object_product()
    assert type(product) is dict
