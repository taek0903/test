# np_module.py

import numpy as np
# ndarray=>n차원 배열, 차원 고려 배열 생성가능
arr = np.array([1,2,3,4,5]) # ㅂ차원 백터
print(type(arr))
print(arr)

print(arr.shape)    # 배열 모양(크기)
print(arr.dtype)    # 데이터 타입

print("0으로 초기화된 배열------------")
zeros = np.zeros((3,3)) # 3행3열
print(type(zeros))
print(zeros)

print("1로 초기화된 배열--------------")
ones = np.ones((2,4))   # 2행4열
print(ones)
print(ones.shape)
print(ones.dtype)

print("값으로 초기화된 배열-----------")
full = np.full((2,2),7)
print(full)

print("단위행렬----------------------")
identity1 = np.eye(3)
identity1 = np.eye(2,3)         # 직사각행렬
print(identity1)
identity2 = np.identity(3)      # 정사각행렬
print(identity2)

print("난수배열----------------------")
# 0이상 1미만 범위의 실수 난수 생성
random = np.random.rand(3,3)
print(random)
print(random.shape)
print(random.dtype)

# 1이상 10미만 범위의 정수 난수 생성
randint = np.random.randint(1,10,(3,3))
print(randint)
print(randint.shape)
print(randint.dtype)

# 랜덤 문자 출력 예시) 문자 => 아스키코드 변환
randint = np.random.randint(ord('a'),ord('z')+1, size=5)
rand_chars = np.array([chr(c) for c in randint])
print(rand_chars)

print("기본 산술 연산-----------------")
arr = np.array([1,2,3,4])
print(arr+5)
print(type(arr+5))
print(arr*2)

print("통계 함수----------------------")
print(arr.sum())    # 총합
print(arr.mean())   # 평균
print(arr.max())    # 최대값   
print(arr.min())    # 최소값

print("브로드캐스팅-------------------")
arr1 = np.array([1,2,3])
print(arr1)
print(arr1.shape)
print('------------------------------')
arr2 = np.array([[1],[2],[3]])
print(arr2)
print(arr2.shape)

# 브로드캐스팅 : 자동으로 (모양을) 맞춰서 늘려준다.
# arr1은 1차원이지만 연산시 (1,3) 처럼 동작
result = arr1+arr2
print(result)

print('행렬 곱------------------------')
# 행렬 곱
matrix1 = np.array([[1,2],[3,4]])
print(matrix1)
matrix2 = np.array([[5,6],[7,8]])
print(result)

print('기본 인덱싱--------------------')
arr = np.array([10,20,30,40])
print(arr[2])

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr[1,2])

print('슬라이싱-----------------------')
print(arr[0,:3])
print(arr[0,:])
print(arr[:,1])

print('조건부 연산--------------------')
arr = np.array([1,2,3,4,5])
print(arr>3)
filtered = arr[arr>3]
print(filtered)
# and,or,not: 파이썬 bool용 => &,|,~: numpy 배열용
filtered1 = arr[(arr>2) & (arr<4)]
print(filtered1)

import pandas as pd
df = pd.DataFrame(arr, columns=['Value'])
print(df)