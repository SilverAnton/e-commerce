class Product:
    """Класс содержит название, описание, цену и количество товара, в наличии"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity_in_stock):
        """Инициализатор названия объекта, описания объекта, цены и количества товаров, в наличии"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock