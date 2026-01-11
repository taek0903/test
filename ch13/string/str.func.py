# str.func.py

# 문자열.split(구분자) -> list 형태 반환

my_string="Python is a popular programing language"
split_list=my_string.split()
print(split_list)
print(split_list[4])

print('------------------')
# 문자열.strip()
my_string="    Python is awesom!     "
stripped_string=my_string.strip()
print(my_string)
print(stripped_string)
print(stripped_string[0])

print('------------------')
# 문자열.join()
my_list = ["apple",'banna', 'cherry']
joined_string="-".join(my_list)
print(joined_string)
print(type(joined_string))

num_list = ["010", '1234', "5678"]
joined_string="-".join(num_list)
print(joined_string)