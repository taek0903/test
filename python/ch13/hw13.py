# hw13.py

# 6번
print('6---------------')
try:
    x = 10/0
except ZeroDivisionError as e:
    print("Cannot divide by zero!")

# 7번
print('7---------------')
try:
    raise KeyError("Missing key")
except KeyError:
    print("Key is missing!")

# 8번
print('8---------------')
add=lambda x,y : x+y
print(add(3,5))

# 9번
print('9---------------')
per = ["10.31","","8.00"]
for i in per:
    try:
        print(float(i))
    except ValueError as e:
        print(type(e),"0")

# 10번
print('10---------------')
numbers = [10,20,30]
for i in range(len(numbers)):
    try :
        print(numbers[int(input("인덱스를 입력하시오"))])
    except ValueError as e:
        print("아라비아 숫자로 입력하시오")
    except IndexError as e:
        print("잘못된 인덱스입니다.")
    