# coding:utf-8

p = lambda:6

print type(p)
print p()

def foo(x,y):
    return x+y

p=lambda x,y:x+y

print foo(5,6)
print p(5,6)