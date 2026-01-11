# tuple1.py

clovers = ('클로버1', '하트2', '클로버3')
print(clovers[1])
print(type(clovers))
print(clovers[0])
print(clovers[1])
print(clovers[2])

my_tuple1=()
print(my_tuple1)

my_tuple2 = (1, -2, 3.14, True, "Hi", [1,2])
print(my_tuple2)

print("---------------------------")
my_tuple3 = 1, -2, 3.14, True, "Hi", [1,2]
print(my_tuple3)
print(type(my_tuple3))

print(my_tuple3[3])
# my_tuple3[3] = False

print(my_tuple3[5])
# my_tuple3[5] = [3,4]

# my_tuple3[5][0] = 3
# print(my_tuple3)

# my_int = (1)
# print(type(my_int))

my_tuple=1,
print(type(my_tuple))

print("---------------------------")
a = (1,2,3)
print(a, "a의 데이터형식은", type(a))
b=list(a)
print(b,"b의 데이터형식은",type(b))
b[0] = 7
print(b)
print(type(b))
a=tuple(b)
print(a, "a의 데이터형식은", type(a))