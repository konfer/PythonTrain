 #coding:utf-8

i=iter("abc")
print type(i)
print i.next()
print i.next()
print i.next()

for item in i:
    print item
    
myList=[3,5,7,8,9]
p=iter(myList)
print type(p)

for item in p:
    print item
    
print [x**2 for x in xrange(10)]
p=(x**2 for x in xrange(10))
print type(p)
for item in list(p):
    print item