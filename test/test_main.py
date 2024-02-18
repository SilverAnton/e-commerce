import src.main

# фикстуры для удобства тестирования кода классов и функций
products = src.main.get_object_category('products.json')
objects = src.main.get_object_product()
phone_description = ('Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для '
                     'удобства жизни')
tv_description = 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником'
phone_names = ['Samsung Galaxy C23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']
tv_name = ['55" QLED 4K']


def test_product():
    """Тест проверяет корректность полученных типов объектов класса Product"""
    assert src.main.Product(objects['name']).name in phone_names or tv_name
    assert src.main.Product(objects['description']).description == str
    assert src.main.Product(objects['price']).price == float
    assert src.main.Product(objects['quantity']).quantity == int


def test_category():
    """Тест проверяет корректность полученных типов объектов класса Category"""
    assert src.main.Category(products['name']).name == 'Смартфоны' or 'Телевизоры'
    assert src.main.Category(products['description']).description == phone_description or tv_description
    assert src.main.Category(products['products']).products == list


def test_get_object_category():
    assert type(products) is dict


def test_get_object_product():
    assert type(objects) is dict