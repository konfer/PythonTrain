#coding:utf-8

class Foo(object):
    
    #pass
    
    def __getattribute__(self,attr):
        print "in __getattribute__"
        return attr
    

p=Foo()

p.__setattr__('x',5)
setattr(p,'y',15)
print p.x
print p.y