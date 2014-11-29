#coding:utf-8

import random
import string

theNum=random.randint(0,100)

while True:
    guess=raw_input("please input a num:\n")
    if guess.isdigit():
        print "bingo"
    else :
        print "sorry"
        