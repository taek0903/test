print(3==5)
print("---------------------")

print((3==3) and (4!=3))
print("---------------------")

if 4<3:
    print("Hello World.")
else:
    print("Hi, there.")
print("---------------------")

if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
print("---------------------")

num1 = input("숫자를 입력하세요: ")
if int(num1) % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
print("---------------------")

num2 = input("숫자를 입력하세요: ")
if int(num2) + 20 > 255:
    print(255)
else:
    print(int(num2)+20)
print("---------------------")

num3 = input("숫자를 입력하세요: ")
if int(num3) > 255:
    print("0~255의 값으로 입력해주세요.")
elif int(num3) >= 20:
    print(int(num3)-20)
elif int(num3) < 20:
    print(0)
else:
    print("0~255의 값으로 입력해주세요.")
print("---------------------")

time = input("시간을 입력해주세요: ")
hour, minute = map(int, time.split(":"))
if minute==0:
    print("정각입니다.")
else:
    print("정각이 아닙니다.")
print("---------------------")

score = input("학점을 입력하세요: ")
if int(score) >= 81 :
    print("grade is A")
elif int(score) >= 61 :
    print("grade is B")
elif int(score) >= 41 :
    print("grade is C")
elif int(score) >= 21 :
    print("grade is D")
else:
    print("grade is E")