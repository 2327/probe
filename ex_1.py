
class ItemDiscount:
    def __init__(self, discount=None):
        self.__x = 5
        self.__y = 'ggg'

        if discount == None:
            discount = 0
        else:
            self.discount = discount

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class ItemDiscountReport(ItemDiscount):
    def __str__(self):
        result = self.get_x() - self.discount
        return str(result)


probe = ItemDiscountReport(discount=3)
print(probe)