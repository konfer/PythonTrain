#coding:utf-8

while True:
    theNum=raw_input("Please input a number:\n")

    if theNum.isdigit():
        num=int(theNum)
        counter=1
        while counter<num:
            innerCounter=counter
            counter+=1
            print 2*(num-counter)*" ",
            while innerCounter>0:
                print innerCounter,
                innerCounter-=1
            print
    else :
        print "invalid number"