#coding:utf-9

file2=open("ipout-3.txt",'w')
list1=[]

with open("ip.txt","r") as f:
    for line in f :
        s=line.find("Sogou web spider")
        
list2=list(set(list1))

for item in list2:
    file2.write(item+'\n')