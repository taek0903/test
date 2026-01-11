print('1----------------------')
def sum_to_n(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total
print(sum_to_n(10))

print('2----------------------')
def even_sum(n):
    total = 0
    for i in range(1,n+1):
        if i % 2== 0:
            total += i
    return total
print(even_sum(10))

print('3----------------------')
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

print('4----------------------')
def count_vowels(s):
    vowels=set('aeiou')
    cnt=0
    for ch in s.lower():
        if ch in vowels:
            cnt += 1
    return cnt

print('5----------------------')
def find_max(nums):
    max_nums=nums[0]
    for i in range(1,len(nums)):
        if nums[i] > max_nums:
            max_nums=nums[i]
    print(max_nums)
a=[3,9,-1,7,2]
find_max(a)

print('6----------------------')
def solve(dic):
    d={}
    for key, value in dic:
        if key in d:
            d[key] += value
        else:
            d[key] = value
    return sum(d.values())
dic =[("a",10),("b",20),("a",5),("c",7)]

print(solve(dic))

print('7----------------------')
def swap(a,b):
    temp=a
    a=b
    b=temp
    print(a,b)

swap(10,20)

print('8----------------------')
lst=[3,6,7,4,9,10,13]
for i in range(0,len(lst),1):
    first_even=None
    if lst[i] % 2 ==0:
        first_even=i
        break
for j in range(len(lst)-1,-1,-1):
    final_odd=None
    if lst[j] % 2 != 0:
        final_odd=j
        break
lst[first_even], lst[final_odd] = lst[final_odd], lst[final_odd]
print(lst)

print('9----------------------')
def selsort(a):
    for i in range(0,len(a)-1):
        min_idx=i
        for j in range(i,len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        temp=a[i]
        a[i]=a[min_idx]
        a[min_idx]=temp
    print(a)
selsort([5,2,4,1,3])

def selsort_down(b):
    for i in range(0,len(b)-1):
        max_idx=i
        for j in range(i,len(b)):
            if b[j] > b[max_idx]:
                max_idx=j
        temp=b[i]
        b[i]=b[max_idx]
        b[max_idx]=temp
    print(b)
selsort_down([5,8,7,9,2,4,10])

def swap_even_odd(lst1):
    even_idx=None
    odd_idx=None
    for i in range(0,len(lst1)):
        if lst1[i] % 2 == 0:
            even_idx=i
            break
    for j in range(len(lst1)-1,-1,-1):
        if lst1[j] % 2 != 0:
            odd_idx=j
            break
    lst1[even_idx], lst1[odd_idx] = lst1[odd_idx], lst1[even_idx]
    print(lst1)
swap_even_odd([1,5,8,7,9,6,8,7,2,3,4])

def find_max_min(lst2):
    max_num_idx=0
    min_num_idx=0
    for i in range(1,len(lst2)):
        if  lst2[max_num_idx] < lst2[i] :
            max_num_idx=i
    for j in range(1,len(lst2)):
        if lst2[min_num_idx] > lst2[j]  :
            min_num_idx=j
    print(lst2[max_num_idx],lst2[min_num_idx])

find_max_min([2,4,6,7,8,1,2,9])

print('11----------------------')
def range_sum(a,b):
    total = 0
    start = min(a,b)
    end = max(a,b)
    for x in range(start,end+1):
        total += x
    print(total)
range_sum(5,1)

print('12----------------------')
def most_frequent_char(s):
    freq = {}

    for ch in s:
        if ch == " ":
            continue
        ch = ch.lower()
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    
    best_char = None
    best_cnt = -1

    for ch, cnt in freq.items():
        if cnt > best_cnt:
            best_cnt = cnt
            best_char = ch
        elif cnt == best_cnt and ch < best_char:
            best_char = ch
    return best_char

s = "A ba aC aa"
print(most_frequent_char(s))



def solution(array):
    freq={}
    for x in array:
        freq[x]=freq.get(x,0)+1
    max_cnt=max(freq.values())
    modes=[]
    for v, cnt in freq.items():
        if cnt == max_cnt:
            modes.append(v)
    if len(modes) >= 2:
        return -1
    return modes[0]