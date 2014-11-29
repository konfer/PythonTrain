#coding:utf-8

def average(averList):
	length=len(averList)
	return reduce(lambda x,y:x+y,averList)/length

print average([1,2,3,5,6])