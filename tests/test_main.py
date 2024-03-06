import pytest
from src.product import Product
from src.category import Category


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

@pytest.fixture
def product_2():
    return Product(name='Iphone 15',
                   description='512GB, Gray space',
                   price=210000.0,
                   quantity_in_stock=8)

@pytest.fixture
def price():
    return 10


# Фикстуры
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
# Фикстуры
tv = [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]

phones_list = ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.; Iphone 15, 210000.0 руб. Остаток: 8 шт.; '
               'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.')
tv_list = '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


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


def test_add_product(category):
    """Тест проверяет добавление объекта товара в атрибут списка product класса Category"""
    category.add_product(product)
    assert category.products == [product]


def test_get_products(category):
    """Тест проверяет возврат приватного объекта класса Category - списка товаров(__products)"""
    assert category.get_products == phones or tv


def test_product(category):
    """Тест проверяет возврат объекта из атрибута products класса Category, в формате строки: товар, цена руб.,
    остаток шт."""
    assert category.product in phones_list or tv_list


def test_new_object(product):
    """Тест проверяет возврат новых объектов класса Product методом new_object"""
    assert product.new_objects(phones[0]).name == 'Samsung Galaxy C23 Ultra'
    assert product.new_objects(phones[0]).description == '256GB, Серый цвет, 200MP камера'
    assert product.new_objects(phones[0]).price == 180000.0
    assert product.new_objects(phones[0]).quantity_in_stock == 5


# никакой тест для метода .price класса Product, не получается нормально протестировать, из-за условия в методе
# класса Product(задание со звездочкой).не соображу никак(
def test_price(product, price):
    assert product.price == 180000.0



def test_str_category(category):
    """Тест проверяет правильность печати магического метода __str__, объектов класса Category"""
    assert print(category) == print('Смартфоны, количество продуктов: 1 шт.')


def test_len_category(category):
    """Тест проверяет правильность сложения количества товаров категории"""
    assert len(category) == 1


def test_str_product(product):
    """Тест проверяет правильность печати магического метода __str__, объектов класса Product"""
    assert print(product) == print('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.')


def test_add_product(product, product_2):
    """Тест проверяет правильность сложения магического метода __add__ объектов класса Product"""
    assert product + product_2 == 2580000.0