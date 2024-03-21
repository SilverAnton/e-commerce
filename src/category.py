from src.product import Product


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
        """Метод добавляет экземпляр товара класса Product в атрибут списка product класса Category"""
        if issubclass(products.__class__, Product):
            cls.products.append(products)
            if products.quantity_in_stock == 0:
                raise ValueError('товар с нулевым количеством не может быть добавлен')

    @property
    def get_products(self):
        """Возвращает приватный объект класса - список товаров"""
        return self.__products

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        """Возвращает строку в формате: категория, количество продуктов: шт."""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    @property
    def product(self):
        """Геттер возвращает объект из атрибута products, в формате строки: товар, цена руб., остаток шт. """
        objects = ''
        products = self.products
        for product in products:
            objects += '; ' + f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт."
        return objects[1:]

    @property
    def products_av_price(self):
        """Возвращает среднюю цену всех добавленных продуктов в виде float"""
        prices = 0
        for product in self.products:
            prices += product.price
        if len(self.products) == 0:
            try:
                return prices / len(self.products)
            except ZeroDivisionError as e:
                print(e)
                return 0
        return prices / len(self.products)
