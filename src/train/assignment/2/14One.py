#coding:utf-8

while True:
    theNum=raw_input("Please input numbers splitted by ',':\n")
    
    theNumList=theNum.split(",");
    theNumList.sort();
    
    print theNumList;
        