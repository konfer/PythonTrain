#coding:utf-8

def findMid(seq):
    seq=sorted(seq)
    print seq
    seqLen=len(seq)
    midIndex=seqLen/2
    if seqLen%2==0:
        return (seq[midIndex]+seq[midIndex-1])/2
    else:
        return seq[int(midIndex)]

myList=[1.0,2.0,3.0,4.0]
print findMid(myList)