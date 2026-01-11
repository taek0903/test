# swapFunc.py

# na와 nb를 입력하는 함수를 작성하시오.
def funca(pa, pb):
    temp = pa
    pa = pb
    pb = temp
    print(f"함수 내 pa 값: {pa}", end=" ")
    print(f"pb 값: {pb}")
    return pa, pb

na=10
nb=11
print(f"na 값은 {na} nb 값은 {nb}")
na, nb = funca(na, nb)
print(f"na 값은 {na} nb 값은 {nb}")