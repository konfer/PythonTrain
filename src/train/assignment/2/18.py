#coding:utf-8

source={"a":1,"b":2}
mergePart={"c":3,"d":4}

afterMerge=dict(source.items()+mergePart.items())

print afterMerge