#coding:utf-8

class Person(object):
    def __init__(self,name,age,height):
        dict1={"work":"python programmer","salary":"13k"}
        self.name=name
        self.age=age
        self.height=height
        self.occupation=dict1

    def getName(self):
        print "My name is "+self.name

    def getAge(self):
        print "I am  %d years old" %(self.age)


    def getHeight(self):
        print "I have {0} metre height".format(self.height)

    def print_salary(self):
        for key in self.occupation:
            print key,self.occupation[key]

p1=Person("Tom",25,1.8)
p1.getName()
p1.getAge()
p1.getHeight()
p1.print_salary()
