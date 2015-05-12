#coding:utf-8

class Foo(object):
    def __init__(self,x):
        self.x=x
        
#a=Foo(5)
tmp=Foo.__new__(Foo,5)
tmp.__init__(5)
print type(tmp)
print tmp.x