#coding:utf-8

def foo(number):
    if number>0:
        return "正数"
    elif number<0:
        return "负数"
    else:
        return "0"
     
print foo(5)  