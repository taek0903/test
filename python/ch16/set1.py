# set1.py
numbers={1,2,3,3,4}
print(type(numbers),numbers)

numbers.add(5)
numbers.remove(3)
print(numbers)

set1={1,2,3}
set2={3,4,5}

print(set1&set2)
print(set1|set2)
print(set1-set2)

# 자동 정렬 안됨 -> sorted()
# 순서 보장 여부 : 보장안됨
numbers = {4,3,5,1,2}
print(numbers)

s=set()
print(type(s))
print(s)
s.add(1)
s.add(2)
s.remove(1)
print(s)
