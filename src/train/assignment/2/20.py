#coding:utf-8

myDict={"a":1,"c":2,"b":5,"e":6,"d":4}

myList=myDict.keys()

keyList=sorted(myList,key=str.upper)

for letter in keyList:
    print letter+":"+str(myDict[letter])
    
items=myDict.items()
print items