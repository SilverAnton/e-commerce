class Category:
    """Класс Category, представляет категории товаров"""
    category_count = 0
    unique_products_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        """Инициатор имени объекта, описания объекта, списка товаров"""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.unique_products_count += len(products)
