numList = [7, 9, 3, 11, 2, 34, 5, 66, 77, 88, 99, 13]

n = len(numList)

for i in xrange(n):
    small = i
    for j in xrange(i + 1, n):
        if numList[j] < numList[small]:
            small = j
    if small != i:
        numList[i], numList[small] = numList[small], numList[i]
        
print numList
