#coding:utf-8

FibonacciList=list()

def addFibonacciListNum(m):
	a,b=0,1
	for i in range(1,m):
		yield b
		a,b=b,a+b

def getFibonacciNum(max,m):
	FibonacciList=list(addFibonacciListNum(max))
	if(m<max):
		return FibonacciList[m]

print getFibonacciNum(20,9)