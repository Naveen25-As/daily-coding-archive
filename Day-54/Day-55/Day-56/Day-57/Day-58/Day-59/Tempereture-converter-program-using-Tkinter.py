# Temperature Converter program using Tkinter.

import tkinter as tk

def convert():
    c = float(entry.get())
    f = (c * 9/5) + 32
    result.config(text="Fehrenheit: "+str(f))

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Convert", command=convert).pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()
