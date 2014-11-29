#coding:utf-8

def find_ip(path):
    urllist=[]
    for line in open(path):
        s=line.find('Sogou ')
        if s>=0:
            urllist.append(line[:s].strip())
    return urllist

list1=find_ip("ip.txt")
print list(set(list1))
# for item in list1:
#     print item


