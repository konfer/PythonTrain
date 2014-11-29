#coding:utf-8

#a
def mult(x,y):
	return x*y

#b
def myFactorial(x):
	return reduce(mult,range(1,x+1))

print myFactorial(4)

#c
def lambdaFactorial(x):
	return reduce(lambda x,y:x*y,range(1,x+1))

print lambdaFactorial(5)

#c
# def lambdaFactorial(x,y):
# 	return reduce(lambda x,y:for _x in xrange(y))