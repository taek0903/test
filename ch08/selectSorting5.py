# selectSorting5.py

ca=[21,10,11,15,13]
cb=[21,10,11,15,13,14]
for sb in range(0,4,1):
    mina = ca[sb]
    minix = sb
    for sc in range(sb+1,5,1):
        if mina > ca[sc]:
            mina = ca[sc]
            minix = sc
    temp=ca[sb]
    ca[sb]=ca[minix]
    ca[minix]=temp
    print(ca)

print('--------------------')
ca=[21,10,11,15,13]
cb=[21,10,11,15,13,14]
def fslesort(lst):
    for i in range(0,len(lst)-1,1):
        mina = lst[i]
        minix = i
        for j in range(i+1, len(lst),1):
            if mina > lst[j]:
                mina = lst[j]
                minix = j
        temp=lst[i]
        lst[i]=lst[minix]
        lst[minix]=temp
    print(lst)
fslesort(cb)
print(len(cb))