# geometry_grid.py

from tkinter import Tk
from tkinter import Button

oroot = Tk()
oroot.geometry("200x100")
obutton1 = Button(oroot, text="PUSH1")
obutton2 = Button(oroot, text="PUSH2")
obutton3 = Button(oroot, text="PUSH3")

obutton1.place(x=10, y=60)
# obutton2.place(x=140, y=60)
obutton2.place(x=50, y=60)
obutton3.place(x=80, y=10)

oroot.mainloop()