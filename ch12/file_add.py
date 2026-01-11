# file_add.py

path = r"python\ch12\file1.txt"
f= open(path, "a", encoding="UTF-8")
# for i in range(11,21):
#     data="%d번째 줄입니다.\n"%i
#     f.write(data)
data=f.read()

print(data)
f.close()