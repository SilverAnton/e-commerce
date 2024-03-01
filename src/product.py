class Product:
    """Класс содержит название, описание, цену и количество товара, в наличии"""
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        """Инициализатор названия объекта, описания объекта, цены и количества товаров, в наличии"""
        self.name = name
        self.description = description
        self._price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def new_objects(cls, products):
        """Метод принимает список товаров и возвращет новые объекты класса Product"""
        objects = []
        for product in products.values():
            objects.append(product)
        name = objects[0]
        description = objects[1]
        price = objects[2]
        quantity_in_stock = objects[3]
        return cls(name, description, price, quantity_in_stock)

    @property
    def price(self):
        """Геттер цены товара"""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер цены товара"""
        if new_price <= 0 or new_price == self._price:
            print('Введена некорректная цена!')
            new_price = self._price
        elif new_price < self._price:
            user_input = str(input('Если вы хотите поменять цену введите: "y", иначе "n"')).lower()
            if user_input == 'y':
                self._price = new_price
            elif user_input == 'n':
                new_price = self._price
            else:
                print("Введено некорректное значение")
        else:
            self._price = new_price
