#coding:utf-8
        
numList=["zero","one","two","three","four","five","six","seven","eight","nine"]


while True:
    theNum=raw_input("Please input a num:\n")
    charList=[]
    zeroFlag=False
    
    if theNum.isdigit():
        num=int(theNum)
        if num>0 and num<1000:
            a=1000
            b=a/10
            while b>=1:
                result=num/b
                if(result!=0):
                    zeroFlag=True
                if zeroFlag==True:
                    charList.append(numList[result])
                num=num%b
                b=b/10
            print "-".join(charList)
        else:
            print "Please input a nun between 0 and 1000"