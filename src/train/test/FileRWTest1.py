#coding:utf-8

file1=open("ip.txt","r")
file2=open("ipout.txt","w")

list1=[]

for line in file1:
    s=line.find('"Sogou web spider')
    if s>=0:
		 list1.append(line[:s].strip())


list2=list(set(list1))

for item in list2:
    file2.write(item+'\n')
    
file1.close()
file2.close()