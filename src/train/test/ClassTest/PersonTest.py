# coding:utf-8

class Person(object):
    age = 18

    def study(self):
        print "18 school"

    def kissing(self):
        print "18 kiss"


p = Person()
print p.age
p.study()
p.kissing()