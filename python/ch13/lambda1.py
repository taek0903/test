# lambda1.py

# def 함수명(매개변수):
#     코드블록
#     return 반환값

# 함수명(인자)

def add(x):
    return x+x
print(add(1))
print(add(2))
print(add(3))

print('------------------')
# lambda 매개변수 : 표현식
# add = lambda x : x + x
# print(add(1))
# print(add(1))
# print(add(1))


print((lambda x : x+x)(1))
print((lambda x : x+x)(2))
print((lambda x : x+x)(3))


print('------------------')
square = lambda x : x**2
print(square(3))
print((lambda x : x**2)(3))

print('------------------')
# lambda 매개1,매개2 : 표현식

adder = lambda x,y=5:x+y # 기본값 설정 가능
print(adder(3,5))
print(adder(3,10))

print((lambda x,y:x+y)(3,10))