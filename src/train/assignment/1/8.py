# coding:utf-8
import math

counter = 0
row = 5
_row = 2 * row - 1

while counter < _row:
    innerCounter = 0
    innerAddCounter = 2 
    counter += 1
    print 2 * (abs(row - counter)) * " ",
    num = 2 * (row - abs(counter - row)) - 1
    while innerCounter < num:
        print "*",
        innerCounter += 1
    print
    
