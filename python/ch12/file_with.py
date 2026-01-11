# file.with.py

# path = r"python\ch12\file2.txt"
# mode = "w"
# f=open(path, mode)

# f.write("No pain, no gain.")

# f.close()

print("-------------------------")
path = r"python\ch12\file2.txt"
mode = "w"
with open(path, mode, encoding="UTF-8") as f:
    f.write("No pain, no gain.\n")
    f.write("노력 없이는, 얻는 것도 없다.\n")

with open(path, "r", encoding="utf-8") as f:
    data=f.read()
print(data)

# 이스케이프(escape) 코드 : 사전 정의된 문자 조합
# \n = new line
# \t = tap
# \b = backspace
# \' = 작은따옴표 표시 ' \' '
# \" = 큰 따옴표 표시 " \" "
# \r = 캐리지리턴(커서를 현주줄의 가장 앞으로 이동)

print("hello\t \"great\"world!!", end="\n")
print(" \bthanks!", end="\n")