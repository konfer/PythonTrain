#coding:utf-8

def foo(*a):
    for i in a:
        print i
        
foo(3,4,5)

b=("sss",78,"de",89)

foo(b)
foo(*b)