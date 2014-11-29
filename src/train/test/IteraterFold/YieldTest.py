#coding:utf-8

def foo():
    yield "hello"
    yield "like"
    yield "python"
    
p=foo()

for item in p:
    print item