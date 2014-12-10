# coding:utf-8

class Foo(object):
    # with ( inherit object new
    pass


class Foo2():
    #not inherit object ;classic
    pass


p = Foo()
Foo.z = 20

print p
p.x = 7
p.y = 8
print p.x
print p.y
print p.z