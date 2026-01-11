# hw11.py

# # 5번
# print('5--------------')
# from tkinter import Tk
# ob=Tk()
# ob.mainloop()

# # 6번
# print('6--------------')
# from tkinter import Tk
# order=Tk()
# order.title("조각 피자 주문 프로그램")
# order.geometry("400x300")
# order.mainloop()

# # 7번
# print('7--------------')
# from tkinter import Tk
# from tkinter import Label
# order=Tk()
# order.title("조각 피자 주문 프로그램")
# order.geometry("400x300")
# orderlabel=Label(order, text="피자")
# orderlabel.pack()
# order.mainloop()

# # 8번
# print('8--------------')
# from tkinter import Tk
# from tkinter import Label
# from tkinter import Checkbutton
# from tkinter import BooleanVar
# order=Tk()
# order.title("조각 피자 주문 프로그램")
# order.geometry("300x400")
# orderlabel=Label(order,text="피자")

# pizza={0:"치즈 피자 (3200원)", 1:"콤비네이션 피자 (3500원)", 2:"불고기 피자 (3600원)"}
# check_value={}

# for i in range(len(pizza)):
#     check_value[i] = BooleanVar()
#     menu=Checkbutton(order, text=pizza[i], variable=check_value[i])
#     menu.pack(anchor="w")

# order.mainloop()

# # 9번
# print('9--------------')
# from tkinter import Tk
# from tkinter import Label
# from tkinter import Checkbutton
# from tkinter import BooleanVar
# from tkinter import Button
# order=Tk()
# order.geometry("400x300")
# order.title("조각 피자 주문 프로그램")
# orderlabel = Label(order, text="피자")
# pizza={0:"치즈 피자 (3200원)",1:"콤비네이션 피자 (3500원)", 2:"불고기 피자 (3600원)"}
# check_value={}

# for i in range(len(pizza)):
#     check_value[i] = BooleanVar()
#     menu=Checkbutton(order, text=pizza[i], variable=check_value[i])
#     menu.pack(anchor="w")

# orbu=Button(order, text="주문")
# orbu.pack()
# order.mainloop()

# 10번
print('10-------------')
from tkinter import Tk, Label, Checkbutton, BooleanVar, Button
order=Tk()
order.geometry("400x300")
order.title("조각 피자 주문 프로그램")
orderlabel = Label(order, text="피자")
pizza={0:"치즈 피자 (3200원)",1:"콤비네이션 피자 (3500원)", 2:"불고기 피자 (3600원)"}
price={0:3200, 1:3500, 2:3600}
check_value={}

for i in range(len(pizza)):
    check_value[i] = BooleanVar()
    menu=Checkbutton(order, text=pizza[i], variable=check_value[i])
    menu.pack(anchor="w")


def show_order():
    total = 0
    lines = ['주문내역']

    for i in range(len(pizza)):
        if check_value[i].get():
            lines.append(f"-{pizza[i]}")
            total += price[i]
    lines.append("")
    lines.append(f"총 가격: {total}원")
    result_label.config(text="\n".join(lines))

orbu=Button(order, text="주문", command=show_order)
orbu.pack()
result_label=Label(order, text="", justify="left")
result_label.pack(pady=10)
order.mainloop()