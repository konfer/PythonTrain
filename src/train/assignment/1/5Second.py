#coding:utf-8

while True:
    theNum=raw_input("Please input a number:\n")

    if theNum.isdigit():
        num=int(theNum)
        while num>0:
            m=1
            while m<num:
                print m,
                m+=1
            num-=1
            print
    else :
        print "invalid number"