from src.category import Category


class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < Category.numb_of_products:
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
