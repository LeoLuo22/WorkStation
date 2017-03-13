# -*- coding:utf-8 -*-

from tkinter import *

def processOK():
    Label(window, text="HelloWorld").pack()
    print("ok button is clicked")

def processCancel():
    print("Cancel is clicked")

window = Tk()
btOK = Button(window, text="ok", fg="red", command="processOK")
btCancel = Button(window, text="Cancel", bg="yellow", command="processCancel")

btOK.pack()
btCancel.pack()

window.mainloop()
