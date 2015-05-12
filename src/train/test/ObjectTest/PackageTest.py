#coding:utf-8

class Foo(object):
    
    def __init__(self,x,y):
        self.__x=x
        self.y=y
        
    def print_x_y(self):
        print self.y
        self.__printxy()
        
    def __printxy(self):
        print "private"
        
p=Foo(5,6)
p.print_x_y()
print p.y


print p._Foo__x

class Foo2(Foo):
    pass

p2=Foo2(5,6)
print p2.y
p2.print_x_y()


        