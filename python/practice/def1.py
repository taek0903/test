# def.py

# def  함수이름 (매개변수):
#     코드블록
#     return 반환값

# def => 새로운 함수를 정의 한다.
# 1. 매개변수가 없는 함수 호출
def fhello(): # fhello() => 실행하면 "매개변수 없는 함수 호출하기" => 출력된다.
    print("매개변수 없는 함수 호출하기")
fhello()
print("-------------")

def fweather(): 
    dica={"아침": 5, "점심":10, "저녁":7} # dic를 정의
    for a, b in dica.items(): # dic 변수 추출 반복 a(key) b(value)
        print(a, "온도는", b, "도이다.")
fweather()
print("-------------")

# 2. 매개변수가 있는 함수 호출
def funca(pa, pb):
    nc=pa+pb
    return nc # return(반환값)을 안작성하고 print함수에 넣으면 none 값이 출력됨
pa=10
pb=11
nd = funca(pa,pb)
print(pa,"+",pb,"=",nd)
print("-------------")

# 3. return 값
a=10
b=20
def fadd(a,b):
    nc = a+b
    return nc
nc=fadd(a,b)
print(a, "+", b, "=", nc)
print("-------------")

def freturn(a,b,c,d):
    dica={a:b, c:d}
    return dica
a="이름"
b="이나경"
c="학점"
d=4.3

dicb=freturn(a,b,c,d)
print(dicb)
print(freturn(a,b,c,d))
print(type(dicb))
print("-------------")

# 함수 정의와 호출
def fabs(arg):
    if(arg<0):
        result=arg*-1
    else:
        result=arg
    return result
print(fabs(10))
print("-------------")

# 함수 호출 순서
def funca(): # 3번째로 동작
    print("funca 함수 호출") # funca 실행
def funcb(): # 2번째로 동작
    funca()  # funcb함수에서 1번째로 실행
    print("funcb 함수 호출") # funcb 함수에서 2번쨰로 실행
def funcc(): # 1번째로 동작
    funcb()  # funcc함수에서 1번째로 실행
    print("funcc 함수 호출") #funcc함수에서 2번째로 실행
funcc()
print("-------------")

def fadd(pa, pb):
    pc = pa+pb
    return pc
def fsub(pa, pb):
    print(fadd(pa, pb))
    pc = pa-pb
    return pc
def fmul(pa, pb):
    print(fsub(pa, pb))
    pc = pa*pb
    return pc
def fdiv(pa, pb):
    print(fmul(pa, pb))
    pc = pa/pb
    return pc

pa=100
pb=3
nc=fdiv(pa,pb)
print(nc)
print("-------------")
def fadd(pa, pb):
    pc = pa+pb
    return pc
def fsub(pa, pb):
    print(fadd(pa, pb))
    pc = pa-pb
    return pc
def fmul(pa, pb):
    print(fsub(pa, pb))
    pc = pa*pb
    return pc
def fdiv(pa, pb):
    print(fmul(pa, pb))
    pc = pa/pb
    return pc
print("-------------")
# pa=int(input("매개변수를 입력하시오: "))
# pb=int(input("매개변수를 입력하시오: "))
# nc= fdiv(pa, pb)
# print(nc)

sta="python example"
def string_length(stb):
    len(stb)
    return len(stb)

lena=string_length(sta)
print(lena)
print("-------------")

# def fdiv(a,b):
#     if b == 0:
#         print("0으로 나눌 수 없다.")
#     div = a / b
#     return div
# a = float(input("숫자를 입력하시오: "))
# b = float(input("숫자를 입력하시오: "))
# c = fdiv(a,b)
# print(fdiv(a,b))
# print("-------------")

def mulsum(a):   
    if a in range(10):
        total = 0
        for i in range(1,101):
            if i % a == 0:
                total += i
        return total
    else:
        return "1부터 9까지의 정수 중 하나를 입력하세요"
b=float(input("배수의 합을 구하고자 하는 정수를 입력하세요."))
print(mulsum(3))     