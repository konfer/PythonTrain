# coding:utf-8

def transTime(myTime):
	s = myTime.find('min')
	timeNum = myTime[ :s ]
	print timeNum
	if timeNum < 1440:
		hour = int(timeNum) / 60
		min = int(timeNum) % 60
		return str(hour) + ":" + str(min)
	else:
		return '时间格式有误'


print transTime('1500min')
