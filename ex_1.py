
class ItemDiscount:
    def __init__(self):
        self.__x = 'a'
        self.__y = 'b'

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.get_x(), self.get_y())

probe = ItemDiscountReport()
probe.set_x('y')
probe.get_parent_data()
