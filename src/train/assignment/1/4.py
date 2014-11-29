#coding:utf-8

header="   1 2 3 4 5 6 7 8 9"
numList=[1,2,3,4,5,6,7,8,9]
headerLength=len(header)

print header
print headerLength*"-"

for i in numList:
    print str(i)+"|",
    for j in numList:
        print i*j,
    print   