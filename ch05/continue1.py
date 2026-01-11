# continue1.py

count = 0
while count < 3:
    count += 1
    if count == 2:
        continue
    print(count)
print('---------------')
# 짝수 출력하기
for i in range(1,6):
    if i % 2 != 0:
        continue
    print(i)

print('---------------')
for i in [1,2,3,4,5]:
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print("*", end="")
    print(end="\n")

print('---------------')
for i in [1,2,3,4,5]:
    for j in [1,2,3,4,5,6,7,8,9,10]:
        print("*", end="")
    print()

print('---------------')
for i in range(5) :
    for j in range(10):
        print("*", end="")
    print()

print(list(range(1,10)))