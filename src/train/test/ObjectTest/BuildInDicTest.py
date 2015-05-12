#coding:utf-8

class Foo(object):
    __slots__=("x","y","z")
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
p=Foo(5,6,7)
p.w=100
print p.w