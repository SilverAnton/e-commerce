from src.product import Product
class Lawn_grass(Product):
    made_in:str
    germ_period:str
    color:str

    def __init__(self,name, description, price, quantity_in_stock, made_in, germ_period, color):
        """Инициализатор названия объекта, описания объекта, цены, количества товара в наличии, страна производитель,
         период прорастания, цвет"""
        self.made_in = made_in
        self.germ_period = germ_period
        self.color = color
        super().__init__(name, description, price, quantity_in_stock)