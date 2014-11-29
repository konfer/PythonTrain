#coding:utf-8

import random

def getFirstDiceValue():
    return random.randint(1,6)

def getSecDiceValue():
    return  random.randint(1,6)

def CrapsDice(playerWinList,bankerWinList):
    first=getFirstDiceValue()
    second=getSecDiceValue()
    sum=first+second
    while True:
        if sum in playerWinList:
            print("玩家赢 筛子和为"+str(sum))
            return
        elif sum in bankerWinList:
            print("庄家赢 筛子和为"+str(sum))
            return
        else:
            print("筛子和为"+str(sum)+"，重新掷筛子")
            CrapsDice([sum],[7])
            return

CrapsDice([7,11],[2,3,12])


