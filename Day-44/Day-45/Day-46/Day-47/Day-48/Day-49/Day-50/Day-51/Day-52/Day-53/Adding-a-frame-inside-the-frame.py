# Adding widgets inside the frame.

import tkinter as tk

root = tk.Tk()
root.title("Frame Example")
root.geometry("300x200")

# Create a frame.
frame1 = tk.Frame(root, bg="blue", padx=20, pady=20)
frame1.pack()

# Add a widget.
label = tk.Label(frame1, text="Welcome")
label.pack()

root.mainloop()
