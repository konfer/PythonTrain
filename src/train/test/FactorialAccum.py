# coding:utf-8

while True:
    total = 1
    sum = 0
    theNum = raw_input("Please input a num:\n")
    
    if theNum.isdigit() :

        for i in xrange(1, int(theNum) + 1):
            total *= i
            sum += total

        print "The FactorialSum of " + str(theNum) + " is " + str(sum) + "\n"

    else :
        print "invalid number\n"
    
