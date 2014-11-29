#coding:utf-8

def foo():
    return 1

print foo()

a_string="this is a global variable"

def foo1():
    print locals()
    
print globals()
print "---------------"

foo1()

a_string="global---"
print id(a_string)

def foo2():
    a_string="local"
    print id(a_string)
    print a_string
    
foo2()

def foo3():
    x=1

foo3()
#print x

print "-----4--------"

def foo4(x):
    print locals()

print foo4(1)

print "------5---------"

def foo5(x,y=0):
    return x-y

print foo5(3)
print foo5(3,1)

print "---6---------"

def outer():
    x=1
    def inner():
        print x
    inner()
    
outer()

print "---------7-----------"

print issubclass(int,object)
print issubclass(list, object)

def foo7():
    pass
print foo7.__class__
print issubclass(foo.__class__,object)

print "----------9-------------"

def outer9(some_func):
    def inner():
        print "before som_func"
        ret=some_func()
        return ret+1
    return inner

def foo9():
    return 1

p=outer9(foo9)
print p()
