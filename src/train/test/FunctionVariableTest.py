#coding:utf-8

x=10

def foo():
    x=7
    print "in inner x=%d" %(x,)
    
foo();

def foo1():
    x=8
    def inner():
        print "in inner x=%d" %(x,)
    return inner

p=foo1()
p()