# Write a GUI program to input a name and password from user and display the same after clicking the button.

from tkinter import*

root = Tk()
root.title("Login Form")

Label(root,text="Name").grid(row=0,column=0)
Label(root,text="Password").grid(row=1,column=0)

name = Entry(root)
password = Entry(root,show="*")

name.grid(row=0,column=1)
password.grid(row=1,column=1)

def display():
    print("Name:",name.get())
    print("Password:",password.get())

Button(root,text="Submit",command=display).grid(row=2,column=1)

root.mainloop()
                                                
                                        
