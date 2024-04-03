# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:21:45 2024

@author: Sungwoo Park
"""

ss = 'Python'

for i in range(0, 6):
    print(ss[i] + '$',end='')
    
####

a = '파이썬 ### CookBook $$$ @@@ 열공중 1234'
b = a.split(' ')
print(b[0] + b[2] + b[5])

####

inStr, outStr = 'Python', ''
strLen = len(inStr)

for i in range(0,strLen):
    outStr += inStr[-i -1]
    
print("내용거꾸로 --> %s"% outStr)


####

import turtle
import random
from tkinter.simpledialog import *
import math

def random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

turtle.title('나선형으로 글자쓰기')
turtle.shape('turtle')
turtle.setup(550, 550)
turtle.screensize(500, 500)
turtle.penup()

instr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
theta = 360*2 / len(instr)
angle = 0
delta = 500/2/len(instr)
radius = 200

for i in instr:
    radian = math.radians(angle)
    tx = radius * math.cos(radian)
    ty = radius * math.sin(radian)
    
    turtle.goto(tx, ty)
    
    turtle.pencolor(random_color()) 
    turtle.write(i, font=('맑은고딕', 20))
    
    angle += theta
    radius -= delta

turtle.done()

    
    

    