# **** Question 1 ****
import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,text="QUIT",fg="red",command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="Hello")
slogan.pack(side=tk.LEFT)
root.mainloop()


# **** Question 2 ****
import tkinter as tk
def msg():
    print("Hello! This is Tkinter. Welcome")
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,text="QUIT",fg="red",command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="Hello",command=msg)
slogan.pack(side=tk.LEFT)
root.mainloop()



# **** Question 3 ****
import tkinter as tk
root = tk.Tk()
w = tk.Label(root, text="Hello Tkinter!")
w.pack()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,text="QUIT",fg="red",command=quit)
button.pack(side=tk.LEFT)
def text():
    print("Let's play with Tkinter")
slogan = tk.Button(frame,text="Hello",command=text)
slogan.pack(side=tk.LEFT)
root.mainloop()


# **** Question 4 ****
from tkinter import *
root = Tk()
Label(root, text="First Name").grid(row=0)
Label(root, text="Last Name").grid(row=1)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
root.mainloop()



