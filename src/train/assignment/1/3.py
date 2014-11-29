#coding:utf-8

while True:
    theNum=raw_input("Please input a number:\n")
    total=0

    if theNum.isdigit():
        num=int(theNum)
        for i in xrange(1,num):
            total+=i
            for j in xrange(1,i+1):
                if(j==1):
                    print j,
                else:
                    print "+"+str(j),
            print "="+str(total),
            print
    else:
        print "invalid Number\n"
    