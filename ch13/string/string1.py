# string1.py

muna = "python"
print(muna[0])
print(muna[1])
print(muna[2])
print(type[muna])
try:
    muna[0]='k'
except TypeError as e: # 문자열 상수
    print(type(e),e)

print('-----------')
munb = ['python']
print(munb[0]) # 문자열이 하나의 요소(item)이다.
print(type[munb])

print('-----------')
munc = ['p','y','t','h','o','n']
print(munc[0])
print(munc[1])
print(munc[2])
print(type[munc])
munc[0]='k'
print(munc)

print('-----------')
for i in range(0,6,1):
    print(munc[i],end="")

length = len(munc)
for i in range(0, length, 1):
    print(munc[i], end="")

print('-----------')
print(ord("A"))
print(ord('a'))
print(chr(97))
print(chr(65))

ma = "ChatGPT" + "를 활용한 python"
print(ma)

language = "python"
print("ChatGPT를 활용한 %s"%language)

language = "python"
print(f"ChatGPT를 활용한 {language}")