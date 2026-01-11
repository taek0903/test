# hw.py

# 3번
arr=[3,6,9,12]
temp = arr[0]
arr[0] = arr[2]
arr[2] = temp
print(arr)
print('---------------')

# 4번
a=[1,2,3]
b=a
print(id(a)==id(b))
print('---------------')

# 5번
x=42
y=42
print(id(x)==id(y))
print('---------------')

# 6번
a=[3,6,7,4,9,10,13]
first_even = None
for find_1st_even in range(len(a)):    
    if a[find_1st_even] % 2 == 0:
        first_even=find_1st_even
        break
last_odd = None    
for find_last_odd in range(len(a)-1,-1,-1):  
    if a[find_last_odd] % 2 == 1:
        last_odd = find_last_odd
        break
a[first_even], a[last_odd]= a[last_odd], a[first_even]
print(a)
print('---------------')

# 7번
a=[3,6,7,4,9,10,13]
def find_max(lst):
    for i in range(len(lst)-1):
        max = lst[i]
        for j in range(1,len(lst)):
            if max < lst[j]:
                max=lst[j]
    return print(max)
find_max(a)

# 10번
def sum_dic(dic):
    total = 0
    for i in dic.values():
        total += i
    return total
data = {'a':10, 'b':20, 'c':30}
print(sum_dic(data))