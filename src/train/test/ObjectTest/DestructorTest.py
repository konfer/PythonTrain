#coding:utf-8

class Foo(object):
    def __init__(self):
        print "init"
        
    def __del__(self):
        print "delete"
        
p1=Foo()
print "-----------"
  