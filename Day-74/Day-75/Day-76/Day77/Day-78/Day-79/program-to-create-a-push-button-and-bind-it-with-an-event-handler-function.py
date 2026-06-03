# Python program to create a push button and bind it with an event handler function using command option.

import tkinter

from tkinter import messagebox

top = tkinter.Tk()

def helloCallBack():
    messagebox.showinfo("Hello Python","Hello world")

B = tkinter.Button(top,text = "Hello",command=helloCallBack)

B.pack()

top.mainloop()
