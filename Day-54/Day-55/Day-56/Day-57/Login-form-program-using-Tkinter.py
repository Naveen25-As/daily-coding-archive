# Login form program using Tkinter.

import tkinter as tk

def login():
    print("Username: ",username.get())
    print("Password: ",password.get())

root = tk.Tk()
root.title("Login form")

tk.Label(root, text = "username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root,text = "Password").pack()
password = tk.Entry(root,show ="*")
password.pack()

tk.Button(root,text = "Login", command = login).pack()

root.mainloop()
