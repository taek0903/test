# hw1.py

# # 2-2
# a=int(input("숫자를 입력해주세요: "))
# b=int(input("숫자를 입력해주세요: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print("----------------")

# # 3-2
# c=int(input("점수를 입력해주세요: "))
# if c >= 90:
#     print("A학점")
# elif c >= 80:
#     print("B학점")
# elif c >= 70:
#     print("C학점")
# else:
#     print("F학점")
# print("----------------")

# 4-1
fruits = ["banana", "peach", "lemon", "grape"]
print(fruits[2])
print("----------------")

# 4-2
student3={"나이":22, "직업":"학생", "취미":"게임"}
student3["도시"]="수원"
print(student3)
print(student3.keys())
print("----------------")

# 5-1
Numbers = [1,2,3,4,5]
for i in Numbers:
    print(i)
print("----------------")

# 5-2
fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']
for j in fruits:
    if j == "사과":
        print("사과를 찾았습니다.")
        continue
    print(j)