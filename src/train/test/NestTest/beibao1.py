#coding:utf-8

def outer():
    w=[8]
    def inner():
        w[0]=w[0]+1
        return w[0]
    return inner

p=outer()
print p()