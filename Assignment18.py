# *** Question 1 ***
import tkinter
F1 = tkinter.Frame()
s = tkinter.Scrollbar(F1)
L = tkinter.Listbox(F1)
s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
L.pack(side=tkinter.LEFT, fill=tkinter.Y)
s['command'] = L.yview
L['yscrollcommand'] = s.set

dict = {"A": 2014,
        "B": 2015,
        "C": 2016,
        "D": 2017,
        "E": 2018}
for name in dict:
   L.insert(tkinter.END, str(name))

F1.pack(side=tkinter.TOP)
F2 = tkinter.Frame()
lab = tkinter.Label(F2)
all_items = L.get(0, tkinter.END)
def poll():
    lab.after(2, poll)
    sel = L.curselection()
    if len(sel)>0:
        item = all_items[sel[0]]
        print(dict[item])
        lab.config(text=str(sel))
lab.pack()
F2.pack(side=tkinter.TOP)
poll()
tkinter.mainloop()

# *** Question 2 ***
import tkinter
F1 = tkinter.Frame()
s = tkinter.Scrollbar(F1)
L = tkinter.Listbox(F1)
s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
L.pack(side=tkinter.LEFT, fill=tkinter.Y)
s['command'] = L.yview
L['yscrollcommand'] = s.set

dict = {"A": 2014,
        "B": 2015,
        "C": 2016,
        "D": 2017,
        "E": 2018}
for name in dict:
   L.insert(tkinter.END, str(name))

F1.pack(side=tkinter.TOP)
F2 = tkinter.Frame()
lab = tkinter.Label(F2)
all_items = L.get(0, tkinter.END)
def poll():
    lab.after(2, poll)
    sel = L.curselection()
    if len(sel)>0:
        item = all_items[sel[0]]
        print(dict[item])
        lab.config(text=str(sel))
lab.pack()
F2.pack(side=tkinter.TOP)
poll()
tkinter.mainloop()