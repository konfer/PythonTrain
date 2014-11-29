#coding:utf-8


def tr(srcstr, dststr, string,ignoreFlag):
    
    tempString=string.lower()
    subTempString=string
    tempSrcStr=srcstr.lower()
    lenSrcStr=len(srcstr)
    
    if ignoreFlag and srcstr not in string:
        return False
        
        
    if ignoreFlag:
        string=string.replace(srcstr,dststr)
    else :
        while tempString.find(tempSrcStr)!=-1:
            #替换
            
            cutIndex=tempString.find(tempSrcStr)
            tempSrc=subTempString[cutIndex:cutIndex+lenSrcStr]
            cutNum=cutIndex+lenSrcStr
            
            string=string.replace(tempSrc,dststr)
            
            tempString=tempString[cutNum:]
            subTempString=subTempString[cutNum:]
        
    
    print string

tr('abcdef','mno','abcdefghi',False)