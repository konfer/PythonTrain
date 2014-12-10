#coding:utf-8

class TestClass(object):
    baseNum=100
    myList=[]

    def testBaseNum(self,number):
        self.baseNum=number

    def print_BaseNum(self):
        print "baseNum, I am instanceVariable:",self.baseNum

myTest=TestClass()
myTest.testBaseNum(20)
myTest.print_BaseNum()

myTest.baseNum+=1
myTest.myList.append("change by new Object")

print myTest.baseNum
print myTest.myList
print TestClass.baseNum
print TestClass.myList

TestClass.baseNum+=1
TestClass.myList.append("change by class")