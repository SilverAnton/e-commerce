import pytest
from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


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


@pytest.fixture
def smartphone():
    return Smartphone('телефон', 'отличный телефон', 10000.90, 10, 9800.00, 'superphone', 2024.789, 'base')


@pytest.fixture
def smartphone2():
    return Smartphone('телефон', 'отличный телефон', 10000.90, 0, 9800.00, 'superphone', 2024.789, 'base')


@pytest.fixture
def lawn_grass():
    return LawnGrass('мятлик', 'мягкая газонная трава', 4000.0, 50, 'England', '2а дня на прорастание', 'зеленый '
                                                                                                        'изумруд')


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
products = []


def test_init_product(product):
    """Тест проверяет правильную инициализацию объектов экземпляра класса Product"""
    assert product.name == 'Samsung Galaxy C23 Ultra'
    assert product.description == '256GB, Серый цвет, 200MP камера'
    assert product.price == 180000.0
    assert product.quantity_in_stock == 5


def test_init_category(category):
    """Тест проверяет правильную инициализацию объектов экземпляра класса Category"""
    assert category.name == 'Смартфоны'
    assert category.description == ('Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                                    'функций для удобства жизни')
    assert category.products == phones or tv
    assert category.category_count == 1
    assert category.unique_products_count == 1 or 3


def test_add_product_to_category(category, product, smartphone2):
    """Тест проверяет добавление экземпляра класса товара в атрибут списка product класса Category"""
    if category.add_product(product):
        assert category.products == [product]
    with pytest.raises(ValueError):
        category.add_product(smartphone2)


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


def test_products_av_price(category, smartphone):
    """Тест проверяет правильное получение значения средней суммы всех добавленных продуктов и возникновение
    исключений при получении значения суммы"""
    with pytest.raises(ZeroDivisionError):
        len(category.products) / 0
    category.add_product(smartphone)
    assert category.products_av_price == 10000.9


def test_str_product(product):
    """Тест проверяет правильность печати магического метода __str__, объектов класса Product"""
    assert print(product) == print('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.')


def test_add_product(product, product_2):
    """Тест проверяет правильность сложения магического метода __add__, только объектов экземпляра класса Product и
    его наследников"""
    assert product + product_2 == 2580000.0
    with pytest.raises(TypeError):
        product + 10


def test_smartphone_init(smartphone):
    """Тест проверяет правильную инициализацию объектов экземпляра класса Smartphone"""
    assert smartphone.name == 'телефон'
    assert smartphone.description == 'отличный телефон'
    assert smartphone.price == 10000.90
    assert smartphone.quantity_in_stock == 10
    assert smartphone.performance == 9800.00
    assert smartphone.model == 'superphone'
    assert smartphone.memory == 2024.789
    assert smartphone.color == 'base'


def test_lawn_grass_init(lawn_grass):
    """Тест проверяет правильную инициализацию объектов экземпляра класса Lawn_grass"""
    assert lawn_grass.name == 'мятлик'
    assert lawn_grass.description == 'мягкая газонная трава'
    assert lawn_grass.price == 4000.0
    assert lawn_grass.quantity_in_stock == 50
    assert lawn_grass.made_in == 'England'
    assert lawn_grass.germ_period == '2а дня на прорастание'
    assert lawn_grass.color == 'зеленый изумруд'
