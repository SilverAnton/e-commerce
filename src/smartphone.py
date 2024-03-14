from src.product import Product

class Smartphone(Product):
    perfomance:float
    model:str
    memory:float
    color:str

    def __init__(self,name, description, price, quantity_in_stock, perfomance, model, memory, color):
        """Инициализатор названия объекта, описания объекта, цены, количества товара в наличии, производитнльность
        устройства, внутренняя память, цвет устройства"""
        self.perfomance = perfomance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity_in_stock)






