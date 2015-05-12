#coding:utf-8

class TimeSixty(object):
    def __init__(self,hr,min):
        self.hour=hr
        self.min=min
        
    def __str__(self):
        return "%d:%d" %(self.hour,self.min)
    
    def __add__(self,other):
        return self.__class__(self.hour+other.hour,self.min+other.min)
    
    
mon=TimeSixty(10,30)
tue=TimeSixty(11,15)

print mon+tue
    

