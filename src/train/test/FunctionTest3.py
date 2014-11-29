#coding:utf-8

def foo1():
    print "in foo1()"
    
def foo2():
    foo1()
    print "in foo2()"
    
def main():
    foo1()
    foo2()
    
if  __name__== "__main__":
    main()