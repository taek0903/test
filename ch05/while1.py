# while1.py

# 변수 초기화
# while 조건식 :
#     코드블록
#     증감식

for num in range(3):
    print('안녕거북이', num)

print("----------------------------")
num= 0
while num < 3:
    print('안녕 거북이', num)
    num = num + 1

# print("----------------------------")
# while True:
#     print('Ctrl+C를 누르세요.')

print("----------------------------")
# 복합대입 연산자

stra="파이썬"
strb="프로그래밍"
stra = stra + strb
print(stra)

stra="파이썬"
strb="프로그래밍"
stra += strb
print(stra)
print("----------------------------")

