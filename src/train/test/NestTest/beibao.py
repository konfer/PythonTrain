#coding:utf-8

def outer():
    x=1
    def inner():
        print x
    return inner

p=outer()
print type(p)
p()

def myOuter(y):
    
    def inner(z):
        print str(y)+":"+str(z)
    return inner

q=myOuter(5)
q(6)