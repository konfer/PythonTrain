# coding:utf-8

class Foo(object):
    def test(self):
        print "in test()"
        print self
        
    @staticmethod
    def foo(x):
        print "in foo()"+x
        
    @classmethod
    def foo2(cls):
        print "in foo2"
        
p=Foo()
p.test()
Foo().test()


Foo.foo("python ")
p.foo("hello")

Foo.foo2()
p.foo2()