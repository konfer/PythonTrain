#coding:utf-8

while True:
    theNum=raw_input("Please input a number:\n")

    if theNum.isdigit():
        num=int(theNum)
        i=1
        while i<num:
            i+=1
            j=1
            while j<i:
                print j,
                j+=1
            print
    else:
        print "invalid number"