#!/usr/bin/python
#coding=UTF8

#Practice 1. Generate number by array

def isAString(number):
    return isinstance(number,str)

def makeNubmers(params):
    count = len(params)
    for a in params:
        for b in params:
            for c in params:
                for d in params:
                    number = str(a) + str(b) + str(c) + str(d)
                    print(number)

makeNubmers([1,2,3,4])