#coding:utf-8


#**代表字典或关键字参数
def foo(**a):
    for item in a:
        print item,a[item]

def foo1(arg1,arg2,*a,**b):
    print "arg1 is",arg1
    print "arg2 is",arg2
    for i in a:
        print i,
    for key in b:
        print key,b[key]
    
        
foo(x=3,y=7)

b={'ff':7,"dd":8}

foo(**b)


foo1(1,2,3,4,x=8,y=9)
foo1(1,2,3,4,a=12,b=17,**{'x':8,'y':9})
