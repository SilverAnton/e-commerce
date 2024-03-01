class Category:
    """Класс Category, представляет категории товаров"""
    category_count = 0
    unique_products_count = 0
    products = []

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        """Инициатор имени объекта, описания объекта, списка товаров"""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.unique_products_count += len(self.__products)

    @classmethod
    def add_product(cls, products):
        """Метод добавляет объект товара в атрибут списка product класса Category"""
        cls.products.append(products)

    def get_products(self):
        """Возвращает приватный объект класса - список товаров"""
        return self.__products

    @property
    def product(self):
        """Геттер возвращает объект из атрибута products, в формате строки: товар, цена руб., остаток шт. """
        objects = ''
        products = self.products
        for product in products:
            objects += '; ' + f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт."
        return objects[1:]
