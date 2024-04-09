# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:30:46 2024

@author: Sungwoo Park
"""

from tkinter import *
from random import *

# 변수 선언 부분
btnList = [""] * 9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
photoList=[None] * 9
i, k=0, 0
xPos, yPos=0, 0
num=0

# 메인 코드 부분
window = Tk()
window.geometry("210x210")

shuffle(fnameList)

for i in range(0,9) :
    photoList[i] = PhotoImage(file="gif/" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])  

for i in range(0,3) :
    for k in range(0,3) :
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()


###############################
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)

    width = photo.width()
    height = photo.height()

    for i in range(height) :
        for k in range(width) :
            r, g, b = photo.get(k, i)
            grey = int((r+g+b)/3)
            photo.put("#%02x%02x%02x" % (grey, grey, grey), (k, i))

    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()


## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상(흑백)")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)





window.mainloop()
