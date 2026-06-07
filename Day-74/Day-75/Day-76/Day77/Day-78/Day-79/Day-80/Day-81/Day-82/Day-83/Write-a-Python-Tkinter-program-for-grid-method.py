# Write a Python Tkinter program for grid method.

import tkinter as tk

root = tk.Tk()

button1 = tk.Button(root, text="Button 1") 
button1.grid(row=0, column=0) 
button2 = tk.Button(root, text="Button 2") 
button2.grid(row=0, column=1)

root.mainloop()
