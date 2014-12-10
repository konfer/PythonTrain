# coding:utf-8

class Foo(object):
    x = 100

    def print_x(self):
        print Foo.x


print Foo.x
Foo.x += 1
print Foo.x
p = Foo()
p.print_x()

print dir(Foo)
print Foo.__dict__
print "_____________________"
print Foo.__name__
print Foo.__module__
print Foo.__bases__
print "-------------"
print Foo.__class__