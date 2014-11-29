# coding:utf-8

numList = [7, 9, 3, 11, 2, 34, 5, 66, 77, 88, 99, 13]

for i in xrange(len(numList)):
    key = numList[i]
    j = i - 1
    while j > -1 and numList[j] > key:
        numList[j + 1] = numList[j]
        j -= 1
        print numList
    numList[j + 1] = key
    
print numList
