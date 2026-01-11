# dfs.py

# 1
# stack=[]
stack=list()
# print(type(stack))
# stack.append(1)
# print(stack)

# 2
# visited = []
visited = list()

# 3
# start_node='A'
# stack.append(start_node)

# while stack != []:
# while lend(stack) != 0:
# while bool(stack) == True:
while stack:
    # 4
    node = stack.pop()

    # 5
    if node not in visited:
        visited.append(node)
        # stack.extend(reversed(graph[node]))

