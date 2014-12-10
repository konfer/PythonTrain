#coding:utf-8

class Foo(object):
    x=1
    myList=[1]

Foo.x+=1
print Foo.x
p=Foo()
print p.x
p.x+=1
p.myList.append(6)
print p.myList
print Foo.myList
print p.x
print Foo.x
# 不可变不可由对象改变