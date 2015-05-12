#coding:utf-8

class Foo(object):
    
    def __init__(self,x):
        
        self.x=x
        
    def __getattr__(self,name):
        if name=="age":
            return 40
        else:
            raise AttributeError,name
        
p=Foo(5)

print p.age
print p.x
print getattr(p,"x")
help(getattr)
        