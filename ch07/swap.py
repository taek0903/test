# swap.py

# # 변수간 데이터 스왑1
na=10
nb=11
print(f"na 값: {na}" ,end=" ")
print(f"nb 값: {nb}")

temp = na
na = nb
nb = temp

print(f"na 값: {na}" ,end=" ")
print(f"nb 값: {nb}")

# # 변수간 데이터 스왑2
na=10
nb=11
print(f"na 값: {na}" ,end=" ")
print(f"nb 값: {nb}")
na, nb = nb, na
print(f"na 값: {na}" ,end=" ")
print(f"nb 값: {nb}")