#coding:utf-8

list1=[2,[5,8,9],[3,[8,9]]]

def flattenList(myList):
    for item in myList:
        if type(item)==list:
            flattenList(item)
        else:
            yield item

def myFlattenList(myList):
    for item in myList:
        if type(item)==list:
             myFlattenList(item)
        else:
            print item

def flattenTest(list2):
    for item in list2:
        if type(item)==list:
            for subItem in flattenTest(item):
                yield subItem
        else :
            yield  item


print list(flattenTest(list1))



