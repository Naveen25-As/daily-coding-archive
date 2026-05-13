# Counter program using Tknter.

import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=str(count))

root = tk.Tk()

label = tk.Label(root,text = "0",font = ("Arial",20))
label.pack()

tk.Button(root,text ="increase", command=increase).pack()
root.mainloop()
