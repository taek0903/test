# pr1224.py

print('1----------------')
per = ["10.31","","abc"]
for i in per :
    try:
        print(float(i))
    except ValueError as e:
        print(0)

print('2----------------')
test = [('10','2'),('10','0'),("ten","2")]
for a,b in test:
    try:
        a=int(a)
        b=int(b)
        print(a/b)
    except ZeroDivisionError as e :
        print("0으로 나눌 수 없다.")
    except ValueError as e :
        print("숫자를 입력하세요.")

print('3----------------')
try:
    x= int("3.14")
except ValueError as e:
    print("에러 내용", e)

print('4----------------')
def check_password(pw):
    if len(pw) < 8:
        raise ValueError("비밀번호는 8자 이상이어야 합니다.")
    return "통과"

tests = ["1234", "abcdefghi"]

for pw in tests:
    try:
        print(check_password(pw))
    except ValueError as e :
        print("검사 실패:",e)

print('5----------------')
name="Jintaek"
score = 92
print(f"{name}님의 점수는 {score}점입니다.")

print('6----------------')
s='python'
print(f'첫 글자:{s[0]}')
print(f'마지막 글자:{s[-1]}')
print(f'첫 글자 코드:{ord(s[0])}')

print('7----------------')
s='abcdefg'
print(s[1:4])
print(s[::-1])
print(s[::2])

print('8----------------')
text = "10,20,30,40"
parts = text.split(",")
nums = [int(p.strip()) for p in parts]
print(nums)
print("합", sum(nums))

print('9----------------')
parts = ["010", '1234', '5678']
phone = '-'.join(parts)
print(phone)

print('10---------------')
# A
numbers = [1,2,3,4]
squared = list(map(lambda x:x**2, numbers))
print(squared)

# B
str_nums=['10','20','30']
int_nums= list(map(lambda x : int(x), str_nums))
print(int_nums)
