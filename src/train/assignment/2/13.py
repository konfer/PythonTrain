#coding:utf-8

import keyword

while True:
    string=raw_input("Please input a String:\n")
    
    keyWordList=keyword.kwlist
    
    if string in keyWordList:
        print "字符串为关键字"
    
    elif len(string)==1:
        print "字符串长度为1"
    else:
        print "字符串长度为："+str(len(string))