# coding:utf-8

class FooTest(object):
    num = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_xy(self):
        print self.x, self.y

    def print_num(self):
        print FooTest.num


p = FooTest(3, 7)
p.print_xy()
p.print_num()
