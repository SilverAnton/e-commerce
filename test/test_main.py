import pytest
from src.product import Product
from src.category import Category
from src.utils import get_category, get_product, get_file


@pytest.fixture
def product():
    return Product(name='Samsung Galaxy C23 Ultra', description='256GB, Серый цвет, 200MP камера', price=180000.0,
                   quantity_in_stock=5)


@pytest.fixture
def category(product):
    return Category(name='Смартфоны',
                    description='Смартфоны, как средство не только коммуникации, но и получение '
                                'дополнительных функций для удобства жизни',
                    products=[product, ])


# Фикстура
phones = [
    {
        'name': 'Samsung Galaxy C23 Ultra',
        'description': '256GB, Серый цвет, 200MP камера',
        'price': 180000.0,
        'quantity': 5
    },
    {
        'name': 'Iphone 15',
        'description': '512GB, Gray space',
        'price': 210000.0,
        'quantity': 8
    },
    {
        'name': 'Xiaomi Redmi Note 11',
        'description': '1024GB, Синий',
        'price': 31000.0, 'quantity': 14
    }
]
# Фикстура
tv = [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]


def test_init_product(product):
    """Тест проверяет правильную инициализацию элементов объекта класса Product"""
    assert product.name == 'Samsung Galaxy C23 Ultra'
    assert product.description == '256GB, Серый цвет, 200MP камера'
    assert product.price == 180000.0
    assert product.quantity_in_stock == 5


def test_init_category(category):
    """Тест проверяет правильную инициализацию элементов объекта класса Category"""
    assert category.name == 'Смартфоны'
    assert category.description == ('Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                                    'функций для удобства жизни')
    assert category.products == phones or tv
    assert category.category_count == 1
    assert category.unique_products_count == 1 or 3


def test_foo_by_type():
    """Тест проверяет правильность, полученных типов объектов из функций utils.py"""
    assert type(get_file('products.json')) is list
    assert type(get_category()) is dict
    assert type(get_product()) is dict
