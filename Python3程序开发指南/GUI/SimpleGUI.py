# -*- coding:utf-8 -*-

from tkinter import *

window = Tk()
label = Label(window, text = "Welcome")#小构件类的第一个参数是父容器
button = Button(window, text = "Click")
label.pack()
button.pack()

window.mainloop()
