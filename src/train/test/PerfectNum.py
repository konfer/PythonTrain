# coding:utf-8

theNum = int(raw_input("please input:\n"))

counter = 1
sum = 0

while counter < theNum:
    
    if theNum % counter == 0:
        sum += counter
    counter += 1
    
if sum == theNum:
    print str(counter) + " is perfectNum"
else:
    print str(counter) + " ? unlucky"
        
    
    
