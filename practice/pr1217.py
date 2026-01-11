# 1. 홀/짝 판별
n=7
if n % 2 ==0:
    print("짝수")
else:
    print("홀수")
print('----------------------')

# 2. 윤년 판별
year = 2000
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) : 
    print("윤년")
else :
    print("평년")
print('----------------------')

# 3. 자릿수 합
n=4286
s=0
while n > 0: #n 값이 0보다 작을때까지 반복
    s +=n % 10 # 10으로 나눈 나머지 더해서 저장
    n //= 10  # 10으로 나눈 몫을 while문 n에 대입해서 반복
print(s)
print('----------------------')

# 4.  1부터 100까지 배수 합
n=10
s=0
for i in range(1,101):
    if i % n == 0: # i를 n값으로 나누었을 때 나머지가 0인 값만 사용
        s += i
print(s)
print('----------------------')

# 5. 모음 개수 새기
str1="I Like python"
vowels=set('aeiou') # set : 집합형 자료 특징 : 중복 자동 제거,순서 없음(인덱스로 접근 못함)
cnt=0
for ch in str1.lower(): #str.lower() : 대문자 소문자로 변환 문자열만큼 ch 반복  
    if ch in vowels: # ch의 값이 vowels에 들어있으면 동작
        cnt += 1
print(cnt)
print('----------------------')

# 6. 첫 짝수와 마지막 홀수 스왑
c=[3,6,7,4,9,10,13]
def swap_evenodd(lst):
    even_index=None # 짝수 인덱스 번호는 None 할당 안됨
    odd_index=None  # 홀수 인덱스 번호는 None 할당 안됨
    for i in range(len(lst)): # i를 lst의 할당된 인수만큼 반복
        if lst[i] % 2 == 0: # lst[i]의 값이 짝수이면
            even_index=i # even_index에 i 인덱스 번호 할당
            break        # 처음 발견되었으니 조건문 탈출
    for i in range(len(lst)-1,-1,-1): # len(lst)를 뒤에서부터 시작하여 반복
        if lst[i] % 2 != 0: # lst[i]의 값이 홀수이면
            odd_index=i     # odd_index에 i 인덱스 번호 할당
            break           # 처음 발견되었으니 조건문 탈출
    lst[even_index], lst[odd_index]=lst[odd_index], lst[even_index]
    print(lst)
swap_evenodd(c)
print('----------------------')

# 7 딕셔너리 값의 총합
def dic_sum(dic):
    total=0
    for i in dic.values(): # dic.values=> dic의 value 값들을 반복 할당
        total += i
    return print(total)

d={"a": 10, "b": 20, "c":30}
dic_sum(d)
print('----------------------')

# 8 10% 할인 함수
def low_price(pr):
    return pr*0.9
e=15000
print(low_price(e))
print('----------------------')

# 9 재귀 카운트다운
def countdown(a):
    if a == 0:  # a값이 0일 때 동작
        return print("완료")
    print(a) # a값 출력
    countdown(a-1) # countdown(a-1) 만약 a값이 5일 경우 4가 출력되서 다시 반복
f=3
countdown(3)
print('----------------------')

# 10 선택정렬
def selsort(lst):
    for i in range(0, len(lst)-1): # lst함수의 값의 갯수-1번 반복 이유 => 인덱스 0부터 시작
        mina=lst[i]                # mina 변수에 lst[i]의 값을 할당
        min_idx=i                  # min_idx에 인덱스 i할당
        for j in range(i+1,len(lst)): # j에 i가 이미 할당 되어있기 때문에 +1을 해줌
            if mina > lst[j]: # mina 값에 lst[i]값이 할당 되어있음 lst[j]랑 비교
                mina = lst[j] # lst[j]가 더 작으면 mina 값을 lst[j]값으로 교체
                min_idx = j   # min_idx 값에 index j 할당
        temp = lst[i]
        lst[i] = lst[min_idx]
        lst[min_idx]= temp
    print(lst)
a=[5,2,4,1,3]
selsort(a)

# for j in range(i+1, len(1st)):
#   if lst[j] < lst[min_idx]: => lst[j]의 값이 lst[min_inx], 즉 lst[i]보다 작을 경우 동작
#       min_indx = j

# 첫 짝수와 마지막 홀수 스왑
def swap_odd_even(lst):
    odd_idx=None
    even_idx=None
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_idx=i
            break
    for j in range(len(lst)-1,-1,-1):
        if lst[j] % 2 != 0:
            odd_idx=j
            break
    lst[even_idx], lst[odd_idx]= lst[odd_idx], lst[even_idx]
    print(lst)
c=[3,6,7,4,9,10,13]
swap_odd_even(c)
