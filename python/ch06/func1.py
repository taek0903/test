# func1.py

# 함수 정의(생성)
# def 함수명(매개변수1, 매개변수2, ...):
#     코드블럭
#     return 반환값

def my_func():
    print('토끼야 안녕')
    print('거북이야 안녕!')
    print('사자야 안녕')

# 함수 호출(사용)
# 함수명(인수1, 인수2, ...)

my_func()
print("------------------------")

def func1(pa, pb, pc):
    print("모니터 출력")

a = 10
b = 10.7
c = "python"

func1(a,b,c)

print("------------------------")
na=10
nb=11
nc=na+nb
print(na,"+",nb,"=",nc)

def fsum(na, nb):
    nc = na + nb
    print(na,"+",nb,"=",nc)
fsum(10, 20)

print("------------------------")
# 함수 정의
def add(num1, num2):
    sum = num1 + num2
    return sum

# 함수 호출
result = add(2,3)
print(result)

def add(num1, num2):
    num1 + num2
    return num1 + num2
print(add(2,3))
print(add(25,35))
