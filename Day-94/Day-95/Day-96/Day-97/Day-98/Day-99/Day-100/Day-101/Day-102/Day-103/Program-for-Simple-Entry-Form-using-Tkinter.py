# Program for Simple Entry Form using Tkinter.

import tkinter as tk

class NameApp:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Enter your name")

        tk.Label(root, text="Name:").pack()
        self.entry = tk.Entry(root)
        self.entry.pack()

        tk.Button(root, text="Submit", command=self.show_name).pack()

    def show_name(self):
        name = self.entry.get()
        tk.Label(self.root, text=f"Hello, {name}!").pack()

root = tk.Tk()
app = NameApp(root)
root.mainloop()
