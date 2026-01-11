# practice.py

switch = '켜짐'
if switch == '켜짐':
    print('조명이 켜졌어요.')
else:
    print('조명이 꺼졌어요.')

print(2>5)
print(2!=5)
print(False)
print(2==5)

# 어떤 웹사이트에 로그인 하려고 함
# 아이디와 암호를 입력하는 프로그램을 작성하시오
# (둘다 일치해야 로그인 가능)

ID = "abcd"
PW = "1234"
user_ID = input("아이디를 입력하시오: ")
user_PW = input("패스워를 입력하세요.")
if user_ID == ID:
    print("아이디가 일치합니다.")
    if user_PW == PW:
        print("패스워드가 일치합니다.")
        print("로그인 되었습니다.")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("아이디가 틀렸습니다.")