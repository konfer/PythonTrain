#coding:utf-8

def outer():
    def inner():
        print "in inner"
    return inner

p=outer()
print type(p)
p()