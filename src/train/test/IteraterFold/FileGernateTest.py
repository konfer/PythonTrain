#coding:utf-8

def find_ip(path):
    urlList=[]
    for line in open(path):
        urlList.append(line[:line.find('"Sougou web spider')].strip())
        
    return urlList

myUrlList=find_ip("ip.txt")
print list(set(myUrlList))