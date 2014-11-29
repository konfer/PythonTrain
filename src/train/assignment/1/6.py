# coding:utf-8

while True:
    theNum = raw_input("Please input a number:\n")

    if theNum.isdigit():
        num = int(theNum)
        if num > 0 and num < 15:
            counter = 1
            while counter < num:
                innerCounter = counter
                innerAddCounter = 2
                counter += 1
                print 2 * (num - counter) * " ",
                while innerCounter > 0:
                    print innerCounter,
                    innerCounter -= 1
                while innerAddCounter < counter:
                    print innerAddCounter,
                    innerAddCounter += 1
                print
        else:
            print "please input a number between 0 and 15"
    else:
        print "invalid number"
