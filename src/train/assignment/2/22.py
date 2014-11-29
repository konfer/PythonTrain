#coding:utf-8

myDict={"a":1,"c":2,"b":5,"e":6,"d":4}

myKeys=myDict.keys()
myValues=myDict.values()

swapList=zip(myValues,myKeys)

swapDict=dict(swapList)

print swapDict