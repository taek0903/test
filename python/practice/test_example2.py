# print('1----------------------')
# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x += 1
#         return x
#     return inner

# f = outer()
# print(f())

# print('2----------------------')
# def add_item(x, items=None):
#     if items is None:
#         items=[]
#     items.append(x)
#     return items

# print(add_item(12))

# print('3----------------------')
# def ok(s):
#     st = []
#     pairs = {')':'(',']':'[','}':'{'}
#     for ch in s:
#         if ch in '([{':
#             st.append(ch)
#         elif ch in ')]}':
#             if not st or st[-1] != pairs[ch]:
#                 return False
#             st.pop()
#     return len(st) == 0

# print('4----------------------')
# rear = 3
# capacity = 5
# rear = (rear+1) % capacity

# print('----------------------')
# pattern = r'^[A-Z]'

# it = iter([1,2])
# print(list(it))
# remain = list(it)
# print(remain)

# for i in range(20):
#     if i==8:
#         break
#     print(i)

# class Beg:
#     def __init__(self):
#         self.data=[]
#     def add(self,x):
#         self.data.append(x)
#     def addtwice(self,x):
#         self.add(x)

# b= Beg()
# b.addtwice(7)
# print(b.data)


