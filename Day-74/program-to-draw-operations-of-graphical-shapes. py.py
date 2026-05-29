# Write a Tkinter program to draw operations of graphical shapes. 


import tkinter as tk 
root = tk.Tk() 
root.title("Canvas Shapes") 
canvas = tk.Canvas(root, width=400, height=300) 
canvas.pack() 
# Line 
canvas.create_line(50,50,200,50) 
# Rectangle 
canvas.create_rectangle(50,80,200,150) 
# Oval 
canvas.create_oval(50,170,200,250) 
# Circle 
canvas.create_oval(220,80,300,160) 
root.mainloop() 
