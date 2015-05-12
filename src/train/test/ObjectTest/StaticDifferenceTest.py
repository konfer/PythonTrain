#coding:utf-8

import time

class Date(object):
    
    def __init__(self,year,month,day):
        
        self.year=year
        self.month=month
        self.day=day
        
    @staticmethod
    def now():
        t=time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
    
    @classmethod
    def nowClass(cls):
        t=time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)

    @staticmethod
    def tomorrow():
        t=time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
    
    

class EuroDate(Date):
    def __str__(self):
        return  "%02d/%02d/%04d" %(self.day,self.month,self.year)


    
a=Date(1957,4,8)
b=Date.now()
c=Date.tomorrow()

print b.year,b.month,b.day
print EuroDate.now()
print "---------"
print EuroDate.nowClass()