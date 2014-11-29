# coding:utf-8

counter = 0
row = 5

while counter < row:
    innerCounter = 0
    innerAddCounter = 2
    counter += 1
    print 2 * (row - counter) * " ",
    num = 2 * counter - 1
    while innerCounter < num:
        print "*",
        innerCounter += 1
    
    print
