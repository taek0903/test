# p2.py

file_path = r"D:\rokey\python\ch15\file.txt"
data = "hello1" \
"hell2o" \
"hello3"

def write_file(file_path):
    with open(file_path, 'w') as file:
        file.write(data)

write_file(file_path)

def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file.readlines():
            yield line.strip()

lines = read_file(file_path)
print(type(lines))
print(next(lines))
for line in lines:
    print(line)