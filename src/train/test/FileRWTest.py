#coding:utf-8

ReadFile=open("ConditionStatement.py","r")
WriteToFile=open("test.txt","w")

list1=[]

while True:
    line=ReadFile.readline()
    s=line.find("Sogou web spider")
    
    if s>=0:
        list1.append(line[:s].strip())
    if not line:
        break
    
list2=list(set(list1))
print len(list2)