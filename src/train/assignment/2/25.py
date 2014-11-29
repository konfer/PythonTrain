#coding:utf-8

import random

def inLst(list):
    listLen=len(list)-1
    return list[random.randint(1,listLen)]

number=2**31-1

N=random.randint(1,100)

lst=[random.randint(0,number+1) for i in range(0,N)]

print lst

M=random.randint(1,N)

sortLst=[inLst(lst) for i in range(0,M)]


l=sortLst
l.sort()
print l

