#coding:utf-8



def getIp():
	file=open('ip.txt','r')
	for line in file:
		s=line.find('"Sogou web spider')
		if s>0:
			yield line[:s]
		if not line:
			break
	file.close()

ipList=getIp()
for ip in ipList:
	print ip