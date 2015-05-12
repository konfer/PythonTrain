#coding:utf-8

class Foo(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def test(self):
        print "in 类 Foo"

class Foo2(Foo):
    def __init__(self,x,y,z):
        print "Foo2 myself"
        super(Foo2,self).__init__(x,y)
        self.z=z
        
    def myTest(self):
        print self.x,self.y
        super(Foo2,self).test()

print issubclass(Foo2,Foo)

#p=Foo2(3,5)
#p.myTest()

p=Foo2 (4,5,6)
p.myTest()

print  Foo2.__bases__
