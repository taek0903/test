def example(a,b=3):
    c = a+b
print(example(5))
print("-------------------")
# 5
def print_hello():
    return print("안녕하세요.")
print("-------------------")
# 6
print_hello()
print("-------------------")
# 7
for i in range(101):
    print_hello()
print("-------------------")
# 8
def greet(name):
    return print("Hello,",name,"!")
greet(input("이름을 입력하세요."))
print("-------------------")
# 10
def multiply(a,b):
    result = a*b
    return result
print(multiply(4,5))
print("-------------------")