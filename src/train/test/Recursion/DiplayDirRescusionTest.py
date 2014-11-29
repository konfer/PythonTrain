#coding:utf-8

import os

def displayDir(dir):
    for i in os.listdir(dir):
        file=os.path.join(dir,i)
        if os.path.isdir(file):
            displayDir(file)
        else:
            print file

displayDir("D:\Aptana Studio 3 Workspace")
    