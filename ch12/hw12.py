#hw12.py

# 4번
print('4------------------')
with open("text.txt","w") as file:
    file.write("Hello World!")
print(file.closed)

# 10번
print('10-----------------')
with open("./pizza_file1.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    name=[]
    for line in data:
        dataList=line.split()
        name.append(dataList[0].strip())
    print(name)