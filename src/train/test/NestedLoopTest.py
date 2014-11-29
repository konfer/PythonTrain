# coding:utf-8

row = 0
column = 0

theNum = int(raw_input("Please input a num:\n"))

i = 1
while i < theNum:
    i += 1
    j = 1
    while j < i:
        print j,
        j += 1
    print
