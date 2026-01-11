# pr1222.py

# 1번
# import tkinter as tk

# root=tk.Tk()
# root.title("첫 tkinter")
# root.geometry("300x150")

# lbl=tk.Label(root, text="안녕하세요!")
# lbl.pack(pady=10)

# btn = tk.Button(root, text="닫기", command=root.destroy)
# btn.pack()

# root.mainloop()

# 2번
# from tkinter import Tk, Label, Entry, Button, StringVar

# root =Tk()
# root.title("입력을 받아 출력")
# root.geometry("350x180")

# name_var = StringVar()

# Label(root, text='이름을 입력:').pack()
# Entry(root, textvariable=name_var).pack()

# out=Label(root, text="여기에 결과가 나와요.")
# out.pack(pady=10)

# def show_name():
#     out.config(text=f"반가워요, {name_var.get()}!")

# Button(root, text="확인", command=show_name).pack
# root.mainloop()

# 3번
# from tkinter import Tk, Label, Button

# root = Tk()
# root.title("카운터")
# root.geometry("250x150")

# cnt=0
# lbl=Label(root, text="0")
# lbl.pack(pady=10)

# def plus():
#     global cnt
#     cnt += 1
#     lbl.config(text=str(cnt))

# Button(root, text="클릭 +1",command=plus).pack()
# root.mainloop()

# 4번
# from tkinter import Tk, IntVar, Radiobutton, Label, Button

# root = Tk()
# root.title("라디오 선택")
# root.geometry("300x200")

# choice = IntVar()
# choice.set(1)

# Radiobutton(root, text="옵션1", variable=choice, value=1).pack(anchor="w")
# Radiobutton(root, text="옵션2", variable=choice, value=2).pack(anchor="w")
# Radiobutton(root, text="옵션3", variable=choice, value=3).pack(anchor="w")

# lbl=Label(root, text="선택: 1")
# lbl.pack(pady=10)

# def show():
#     lbl.config(text=f"선택: {choice.get()}")
# Button(root, text="확인", command=show).pack()
# root.mainloop()

# 5번
from tkinter import Tk, Checkbutton, Label, Button, BooleanVar

root=Tk()
root.title("체크 선택")
root.geometry("300x200")

v1=BooleanVar()
v2=BooleanVar()
v3=BooleanVar()

Checkbutton(root, text="치즈", variable=v1).pack(anchor='w')
Checkbutton(root, text="페퍼로니", variable=v2).pack(anchor="w")
Checkbutton(root, text="버섯", variable=v3).pack(anchor="w")

lbl=Label(root, text="선택한 토핑: 없음")
lbl.pack(pady=10)

def show():
    picked = []
    if v1.get(): 
        picked.append("치즈")
    if v2.get():
        picked.append("페퍼로니")
    if v3.get():
        picked.append("버섯")
    lbl.config(text="선택한 토핑: " + (", ".join(picked) if picked else "없음"))

Button(root, text="확인", command=show).pack()
root.mainloop()