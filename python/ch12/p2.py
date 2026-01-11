# p2.py

path=r"python\ch12\file3.txt"
with open(path, 'r', encoding="utf-8") as f:
    lines = f.readlines()
    accountlist = []
    for line in lines :
        lineList=line.split(' ')
        print(lineList[1].strip())
        accountlist.append(lineList[1].strip())
print(accountlist)
