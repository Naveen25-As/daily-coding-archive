# Creating a frame.

import tkinter as tk

root = tk.Tk()
root.title("Frame Example")
root.geometry("300x200")

# creating a frame.
frame1 = tk.Frame(root,bg="lightblue",padx=20,pady=20)
frame1.pack()

root.mainloop()
