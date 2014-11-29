 #coding:utf-8

def outer(some_func):
    def inner():
        print "before some_func"
        ret=some_func()
        return ret+1
    return inner

def foo():
    return 1

p=outer(foo)
print type(p)
p()
print p()

@outer
def foo1():
    return 1


print "-------------"
print foo1()


print "------------11---------"

def one(*args):
    print args
    
one()
one(1,2,3)

def two(x,y,*args):
    print x,y,args

two(3,4,6)

def add(x,y):
    return x+y

lst=[1,2]
print add(lst[0],lst[1])
print add(*tuple(lst))

def foo2(**kwargs):
    print kwargs
    
foo2()
foo2(x=1,y=2)

dict1={'a':10,"b":"hello python"}
foo2(**dict1)

print "------------12---------"

def logger(func):
    def inner(*args,**kwargs):
        print "Argumnets were:%s,%s" %(args,kwargs)
        return func(*args,**kwargs)
    return inner

@logger
def foo3(*args,**kwargs):
    print args
    print kwargs


print foo3(5,8,6)

print "-------------13----------------"
def add13(x,y):
    return x+y

lst=[1,2]
print add13(lst[0],lst[1])
print add13(*lst)
print add13(*tuple(lst))

print "-------------14----------------"

def foo13(**kwargs):
    print kwargs
    
foo13()
foo13(x=1,y=2) 
    
dict1={'a':10,'b':"hello python"}
foo13(**dict1)