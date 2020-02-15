
class ItemDiscount():
    def __init__(self, x='a', y='b'):
        self.x = x
        self.y = y


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.x, self.y)

probe = ItemDiscountReport()
probe.get_parent_data()
