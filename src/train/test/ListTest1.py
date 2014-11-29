# coding:utf-8
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list2 = list()

list1.append("hello")
list1.append(5)

for item in list1:
    print item
    
print list1[0]
print "----------------"
print list1[0:8:3]
print list1[-6:-2]
print list1[-1:-9:-2]

list1.extend(["jfids", 4])
print list1
print list1.append("r3")

list1.insert(3, "index3")
print list1

print list1.index("hello")
print list1.index("he")
print "-----------index--------------"

print list1.count(5)
list1.remove("index3")
print list1
print list1.pop(3)

print list1.reverse()

list2 = ["+"]
list3 = list1 + list2
print list3

list4 = list("go")
print list4

print list1

print dir(list)

del list1[2]
print list1

print "-------sort-----------"
list5 = [9, 87, 22, 21, 42, 11]
list5.sort()
print list5

list5 = [9, 872, 22, 213, 42, 11]
strs = ['c', 'dfd', 'fjidfjid', '33', 'ER', 'XD']
list6 = sorted(strs, key=len)
print list6
list6 = sorted(strs, key=str.upper)
print list6
list6 = sorted(strs, key=str.lower)
