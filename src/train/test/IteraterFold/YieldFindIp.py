#coding:utf-8

def find_ip(path):
    for line in open(path):
        s=line.find('"Sogou web spider')
        if s>0:
            yield line[:s].strip()

p=find_ip("ip.txt")
print p.next()