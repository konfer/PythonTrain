qq                  #coding:utf-8

def foo(x,y):
    return x,y

a,b=foo(3,5)

print a,b
print foo(7,8)
print foo(y=9,x="hello")