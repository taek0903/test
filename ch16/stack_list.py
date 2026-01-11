# stack_list.py
# 스택 구현 :리스트 활용

stack=[]

# push 기능 구현
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(f'stack= {stack}')

# pop 기능 구현
stack.pop()
print(f'stack= {stack}')
print(stack.pop())
print(f'stack= {stack}')
stack.pop()

# 스택이 비어있는 경우,
if stack == []:
    print('is empty')

# 스택 꼭대기 값 확인
print(f'stack= {stack}')
print(f'top data= {stack[-1]}')

stack.pop()
if stack == []:
    print('is empty')
else:
    # 스택 꼭대기 값 확인
    print(f'top data= {stack[-1]}')

