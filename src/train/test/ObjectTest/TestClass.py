# coding:utf-8

class TestClass(object):
    
    count=100
    myList=[]
    
    def testCount(self,number):
        self.count=number
        
    def print_count(self):
        print "count:",self.count
        
myTest=TestClass()
myTest.testCount(20)
myTest.print_count()
    
myTest.count+=1
myTest.myList.append("append by myTest")

print myTest.count
print myTest.myList
print TestClass.count
print TestClass.myList

TestClass.count+=1
TestClass.myList.append("change by TestClass")

print myTest.count
print TestClass.count