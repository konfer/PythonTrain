# coding:utf-8

class FindIp(object):
    
    def __init__(self,path):
        self.txtfile=path
        
    def getSougouIp(self):
        ipFile=open(self.txtfile,"r")
        ipList=[]
        for line in ipFile:
            ss= line.find('"Sogou web spider')
            if ss>0:
                ipList.append(line[:ss])
        return ipList
    
p=FindIp("ip.txt")
sogouIp=p.getSougouIp()
print list(sogouIp)