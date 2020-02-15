
class ItemDiscount():
    def __init__(self, x='a', y='b'):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.get_x(), self.get_y())

probe = ItemDiscountReport()
probe.get_parent_data()
