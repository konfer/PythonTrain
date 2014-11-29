# coding:utf-8

rowNum = 9
n = 0

counter = 1

while n < rowNum:
    temp = n + 2
    print str(counter) + "*8+" + str(n + 1) + "= " + str(counter * 8 + n + 1),
    counter = counter * 10 + temp
    n += 1
    print
