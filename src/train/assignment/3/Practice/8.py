#coding:utf-8

def filterLeapYear(yearList):
	return filter(lambda x:x%4==0,yearList)

print(filterLeapYear([1993,1992,2000,2008]))