# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:54:19 2024

@author: Sungwoo Park
"""

def plus(v1,v2,v3):
    result = 0
    result = v1+v2+v3
    print(result)
    
hap = plus(100,200,300)




#######
def f1():
    print(var)
    
def f2():
    var =10
    print(var)
    
var=100
f1()
f2()
##############

def addNumber(num):
    
    sum1 = num * (num+1) /2
    print(sum1)
    
print(addNumber(100))

##########
def myFunc(p1=2, p2=2, p3=2):
    ret = p1 + p2 + p3
    return ret

print(myFunc())  # 출력: 6


def myFunc(p1=2, p2=2, p3=3):
    ret = p1 + p2 + p3
    return ret

print(myFunc(1))  # 출력: 6

def myFunc(p1=2, p2=2, p3=3):
    ret = p1 + p2 + p3
    return ret

print(myFunc(1,2))  # 출력: 6

def myFunc(p1=2, p2=2, p3=2):
    ret = p1 + p2 + p3
    return ret

print(myFunc(1,2,3))  # 출력: 6





