#coding:utf-8

def max(a,b):
	if a>b:
		return a
	else:
		return b

def min(a,b):
	if a<b:
		return a
	else:
		return b

def my_max(myList):
	maxItem=None
	for item in myList:
		maxItem=max(item,maxItem)
	return maxItem

def my_min(myList):
	minItem=myList[0]
	for item in myList:
		minItem=min(minItem,item)
	return minItem


#
NumList=[3,5,9,2,4,1]
WordList=['a','x','b''l']

print my_max(NumList)
print my_max(WordList)
print my_min(NumList)
print my_min(WordList)

