#coding：utf-8

class Person(object):
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def saveMoney(self):
        #print "工资：{0}元"。format(self.salary、2.0)
        print "salary:{0}".format(self.salary/2.0)
        
    def consume(self):
        return self.salary/2.0
    
    def consume_total(self):
        consume_rentHouse=1000
        consume_total=1200
        
        if consume_rentHouse+consume_rentHouse>self.consume():
            print "消费超标"
        else:
            print "else"
            
foo=Person(8000)
foo.comsume_total()