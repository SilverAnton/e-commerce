from src.product import Product


class Smartphone(Product):
    performance: float
    model: str
    memory: float
    color: str

    def __init__(self, name, description, price, quantity_in_stock, performance, model, memory, color):
        """Инициализатор названия объекта, описания объекта, цены, количества товара в наличии, производительность
        устройства, внутренняя память, цвет устройства"""
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity_in_stock)
