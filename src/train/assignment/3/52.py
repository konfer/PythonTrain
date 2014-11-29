#coding:utf-8



def getIp():
	file=open('ip.txt','r')
	for line in file:
		s=line.find('"Sogou web spider')
		if s>0:
			print(line[:s])
		if not line:
			break
	file.close()

getIp()