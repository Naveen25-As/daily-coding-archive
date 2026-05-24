# Write a Tkinter program to draw operations of graphical shapes.

from tkinter import*

root = Tk()
c = Canvas(root,bg = "white",height=700,width=1200)

# create sun
c.create_oval(50,50,200,200,fill="orange")

#create house
c.create_polygon(600,250,700,200,800,250,800,400,600,400,width=2,fill="blue",outline="red")
c.create_line(600,250,800,250,width=2,fill="red")
c.create_rectangle(650,275,750,375,width=2,fill="pink")

# create bushes
c.create_arc(800,350,1000,450,start=0,extent=180,fill="green")
c.create_arc(600,350,400,450,start=0,extent=180,fill="green")
c.pack()
root.mainloop()
