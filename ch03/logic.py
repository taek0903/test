# logic.py

# 논리연산자

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("----------------")

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("----------------")

print(not True)
print(not False)
print("----------------")

print(1 and 1)
print(1 and 0)
print(0 and 1)
print(0 and 0)
print("----------------")

print(1 or 1)
print(1 or 0)
print(0 or 1)
print(0 or 0)

print(9>4 and 3>2)
print(9<4 and 3>2)
print(9<4 or 3<2)
print(9>4 or 3<2)

# 문제1
print(9>4 or 3<2 and 4>2)

# 문제2 괄호>산술>비교>논리
print((3-5)+3<1 and 3-5>1)