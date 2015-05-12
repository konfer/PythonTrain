#coding:utf-8

class Foo(object):
    num=5
    def __init__(self,x,y):
        self.x=x
        self.y=y
    

p=Foo(5,6)
print isinstance(p,Foo)
print isinstance(p,object)

print getattr(p,'x')
print getattr(Foo,'num')
print hasattr(p,"x")
print hasattr(Foo,'num')
setattr(p,'z',8)
print p.z
delattr(p,'z')
print hasattr(Foo,'z')

print dir(p)
print "------------"
print vars(p)
print vars(Foo)