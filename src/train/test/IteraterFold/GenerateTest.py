#coding:utf-8

def foo():
    yield "hello"
    yield "like"
    yield "python"
    
print type(foo())
p=foo()

p=foo()
print p.next()
print p.next()
print p.next()