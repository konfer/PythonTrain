#coding:utf-8


while True:
    string=raw_input("Your string to encrypt was:\n")
    
    rotString=''
    
    for s in string:
        num=ord(s)
        if num >=65 and num<78 :
            num+=13
        elif num>=78 and num<=90:
            num-=13
        elif num>=97 and num<110:
            num+=13
        elif num>=110 and num<122:
            num-=13
        
        rotString+=chr(num)
    
    print rotString