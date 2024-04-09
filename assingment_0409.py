from tkinter import *

window = Tk()

def rdo_change():
    if var.get() == 1:
        label1.configure(text='벤츠')
    else:
        label1.configure(text='포르쉐')
        
var = IntVar()
rdo1 = Radiobutton(window, text='벤츠', variable=var, value=1, command=rdo_change)
rdo2 = Radiobutton(window, text='포르쉐', variable=var, value=2, command=rdo_change)
label1 = Label(window, text='선택한 차량', fg='red')

rdo1.pack()
rdo2.pack()
label1.pack()

window.mainloop()

######

button1 = Button(window, text = '1')
button2 = Button(window, text = '2')
button3 = Button(window, text = '3')
button1.pack(side = LEFT) #LEFT, RIGHT, TOP, BOTTOM
button2.pack(side = LEFT)
button3.pack(side = LEFT)

window.mainloop()

########
from time import *
from tkinter import *

fnameList = ['1','2','3','4','5','6','7','8','9']

num = 0

def clickNext():
    global num
    num+=1
    if num > 8 :
        num = 0
    pLabel.configure(text = fnameList[num])
    
def clickPrev():
    global num 
    num -=1
    if num < 0:
        num = 8
    pLabel.configure(text = fnameList[num])
    
window  = Tk()
window.geometry('500x500')
btnPrev = Button(window, text = '<<이전', command = clickPrev)
btnNext = Button(window, text = '다음>>', command = clickNext)

pLabel = Label(window, text = fnameList[0])
#pLabe
btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)       

window.mainloop()



