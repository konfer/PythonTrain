#coding:utf-8

items={(3,2),(5,7),(1,9),0,(1)}

#print type(items[0])

t=tuple({"a","b"})
print type(t)

list1=list(t)
list1.append("c")

t=tuple(list1)
print t

a=(1)
b=(1,)

print type(a)
print type(b)

x=[1,2,3,4,5]
y=x[:]

print x
print y