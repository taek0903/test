# geometry_grid.py

from tkinter import Tk
from tkinter import Button

oroot = Tk()
oroot.geometry("200x100")
obutton1 = Button(oroot, text="PUSH1")
obutton2 = Button(oroot, text="PUSH2")
obutton3 = Button(oroot, text="PUSH3")

obutton1.pack(side="left")
obutton2.pack(side="right")
obutton3.pack(side="top")

oroot.mainloop()