#coding:utf-8

import time

def funcDetection(func,*args):
	beginTime=time.time()
	retval=func(*args)
	endTime=time.time()
	intervalTime=endTime-beginTime
	return "返回值为："+str(retval)+" 消耗时间为："+str(intervalTime)

def loop(a,b):
	for x in xrange(a):
		b=b+b

	return b

print funcDetection(loop,100000,5)
