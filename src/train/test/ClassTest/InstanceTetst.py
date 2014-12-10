# coding:utf-8

class Foo(object):
    num = 10

    def __init__(self, x, y=8):
        self.x = x
        self.y = y

    def print_x_y(self):
        return self.x+self.y+self.num

p = Foo(5, 6)
print p.print_x_y()

p=Foo(5)
print p.__dict__
print p.__class__
print "----------------"

vars(p)