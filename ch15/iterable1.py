# iterable1.py

a = [1, 2, 3]
# next(a)
# 'list' object is not an iterator

# 이터레이터 생성 방법1: iter() 함수 사용
ia = iter(a)
# print(type(ia))
# print(next(ia))
# print(next(ia))
# print(next(ia))
# print(next(ia))     # StopIteration

for i in ia:
    print(i)

for i in ia:
    print(i)

# print(next(ia))       # StopIteration 

print("------------------")
# 객체의 속성을 보여주는 함수
print(dir(a))
print('__iter__' in dir(a))
print('__next__' in dir(a))

print("------------------")
print(dir(ia))
print('__iter__' in dir(ia))
print('__next__' in dir(ia))
