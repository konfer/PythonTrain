#coding:utf-8

class People(object):
    
    def __init__(self,name):
        self.name=name
        
    def printName(self):
        print "In people类中，My name is %s",(self.name)
        
class Man(object):
    
    def __init__(self,name):
        self.name=name
        
    def printName(self):
        print "in Man class,My name is %s" ,(self.name)
        
for p in [People("aaa"),Man("BBB")]:
    p.printName()