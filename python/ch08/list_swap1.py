# list_swap1.py

ca=[10,11]
print(f"ca[0]의 값은 {ca[0]} ca[1]의 값은 {ca[1]}")
temp=ca[0]
ca[0]=ca[1]
ca[1]=temp
print(f"ca[0]의 값은 {ca[0]} ca[1]의 값은 {ca[1]}")

print('---------------------')
def funca(na, nb):
    temp=na
    na=nb
    nb=na
ca=[10,11]
print(f"ca[0] 값은 {ca[0]} ca[1] 값은 {ca[1]}")
funca(ca[0], ca[1])
print(f"ca[0] 값은 {ca[0]} ca[1] 값은 {ca[1]}")

print('---------------------')
ca=[10,11]
cb=ca
print(f"리스트ca 값은 {ca}")
print(f"리스트cb 값은 {cb}")

print('---------------------')
ca=[10,11]
cb=ca
print(f"리스트ca 값은 {ca}")
print(f"리스트cb 값은 {cb}")
temp=cb[0]
cb[0]=cb[1]
cb[1]=temp
print(f"리스트ca 값은 {ca}")
print(f"리스트cb 값은 {cb}")
print(f"ca[0]={ca[0]} ca[1]={ca[1]}")
print(f"cb[0]={cb[0]} cb[1]={cb[1]}")

print('---------------------')
def funca(cb):
    print(f"리스트 cb 주소 {id(cb)}")
    temp=cb[0]
    cb[0]=cb[1]
    cb[1]=temp
ca=[10,11]
print(f"ca[0]={ca[0]} ca[1]={ca[1]}")
print(f"리스트 ca 주소 {id(ca)}")
funca(ca)
print(f"ca[0]={ca[0]} ca[1]={ca[1]}")

print('---------------------')
def fk(cb):
    total=0
    for sb in range(0,3,1):
        total += cb[sb]
    cb[2]=total
    return cb
ca=[10,20,30]
print(ca)
cd=fk(ca)
print(ca)
print(cd)