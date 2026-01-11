# local1.py

# b=0
# print(f"b의 값 {b}")
# b=1
# print(f"b의 값 {b}")

# def scope_test():
#     global a
#     a = 1  # 지역변수
#     print(f"함수 안의 a 값: {a}")
    
# a=0 # 전역변수
# print(f"함수 밖의 a 값: {a}")
# scope_test()
# print(f"함수 호출 후 a 값: {a}")
# print("----------------------------")
# b=0
# print(f"b의 값 {b}")
# b=1
# print(f"b의 값 {b}")

# def scope_test():
#     global a
#     global b
#     a = 1  # 지역변수
#     b = 2  # 지역변수 선언 전에 작성할 것!!!
#     print(f"함수 안의 a 값: {a}")
    
# a=0 # 전역변수
# print(f"함수 밖의 a 값: {a}")
# scope_test()
# print(f"함수 호출 후 a 값: {a}")
# print(f"함수 호출 후 b 값: {b}")

print("----------------------------")
def scope_test():
    global a
    print(f"a 값 {a}")
    a = 456        # 전역변수
    # a = a+3      # 지역변수
    print(f"함수 안의 a 값: {a}")
    
a=0 # 전역변수
a=123 # 전역변수
print(f"함수 밖의 a 값: {a}")
scope_test()
print(f"함수 호출 후 a 값: {a}")

# 파이썬에서 전역변수는 함수 내부에서 읽기(read) 가능
# 하지만 ! "쓰기(write)"를 하려면 global 키워드 필요!!
