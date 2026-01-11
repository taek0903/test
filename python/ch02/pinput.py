# pinput.py

print("첫 번째 정수를 입력하세요")
ra = input()
ra = int(ra)
print(type(ra))
rb = input("두 번째 정수를 입력하세요")
rb = int(rb)
print(type(rb))
rc = ra+rb # 숫자 + 문자 => Error
print(ra, "+", rb, "값은", rc, "이다.")
