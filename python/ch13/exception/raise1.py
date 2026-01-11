# raise1.py

# try:
#     코드블록(예외 발생 가능성이 있는 코드)
#     raise 예외클래스명('구체적 예외 정보')
# except 예외클래스명:
#     코드블록-예외 처리 코드

try:
    raise NameError('Hi There')
except ValueError as e:
    print('ValueError')
    print(e)
except NameError as e:
    print('An exception flew by!')
    print(e)