# dict2.py

# 변수의 형태는 r_value로 결정
my_data = {"이름":"임진택", "나이": 29, "성별":"남자", "취미":['게임', '농구']}
print(my_data)

items = my_data.items()
print(items)
print(type(items))

keys = my_data.keys()
print(keys)
print(type(keys))

values = my_data.values()
print(values)
print(type(values))