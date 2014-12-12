#coding:utf-8

class FindIp(object):

    ipList=[]
    outList=[]

    def __init__(self,path,keyWord):
        self.txtFile=path
        self.keyWord=keyWord

    def getSougou(self):
        myFile=open(self.txtFile,"r")
        for line in myFile:
            ss=line.find(self.keyWord)
            if ss>0:
                self.ipList.append(line[:ss])
        myFile.close()
        return self.ipList

    def getSougouMethod(self):
        myFile=open(self.txtFile,"r")
        _ipList=myFile.readlines()
        for item in _ipList:
            ss=item.find(self.keyWord)
            if ss>0:
                self.outList.append(item[:ss].strip())
        myFile.close()
        return self.outList



p=FindIp("ip.txt","Sogou web spider")
# dataList=p.getSougou()
dataList=p.getSougouMethod()
print list(set(dataList))


