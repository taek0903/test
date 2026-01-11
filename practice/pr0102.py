print('-1 dfs-')
def dfs_recursive(graph,start):
    stack = list()
    visited = list()
    stack.append(start)
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited
g = {
    1:[2,3,4], 
    2:[1,5], 
    3:[1,6], 
    4:[1,6], 
    5:[2,6], 
    6:[3,4,5]
    }
print(dfs_recursive(g,1))

print('-2 bfs-')
def bfs_order(graph,start):
    queue=list()
    visited=list()
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
print(bfs_order(g,1))

print('-3 bfs 최단거리+최단경로-')
def bfs_shortest_path(graph, start, goal):
    queue=[start]
    head=0
    dist = {start:0}
    parent={start:None}

    while head < len(queue):
        v = queue[head]
        head += 1

        if v == goal:
            break

        for nxt in graph[v]:
            if nxt not in dist:
                dist[nxt] = dist[v]+1
                parent[nxt]=v
                queue.append(nxt)
    if goal not in dist:
        return -1,[]
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return dist[goal], path
g = {
    "A":["B","C"],
    "B":["A","D","E"],
    "C":["A","F"],
    "D":["B"],
    "E":["B","F"],
    "F":["C","E"]
}
distance, path = bfs_shortest_path(g, "A", "F")
print("최단거리:", distance)
print("최단경로:", path)

print('-4 2차원 미로-')
def maze_shortest_steps(maze,start,goal):
    n=len(maze)
    m=len(maze[0])

    sr, sc = start
    gr, gc = goal

    if maze[sr][sc] == 1 or maze[gr][gc] == 1:
        return -1
    dist =[[-1] * m for _ in range(n)]
    dist[sr][sc]

    queue = [(sr,sc)]
    head = 0

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while head < len(queue):
        r,c =  queue[head]
        head += 1

        if (r,c) == (gr,gc):
            return dist[r][c]
        
        for dr, dc in directions:
            nr, nc = r +dr, c+ dc

            if 0 <= nr < n and 0 <= nc < m:
                if maze[nr][nc] == 0 and dist[nr][nc]==-1:
                    dist[nr][nc] = dist[r][c]+1
                    queue.append((nr,nc))
    return -1

maze = [
    [0,0,1,0,0],
    [1,0,1,0,1],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
]
print(maze_shortest_steps(maze, (0,0), (4,4)))

print('-5 연결 요소 개수 세기-')
def count_components(graph):
    visited = set()
    components = 0

    for node in graph:
        if node not in visited:
            components += 1
            queue = [node]
            head = 0
            visited.add(node)

            while head < len(queue):
                v = queue[head]
                head +=1

                for nxt in graph[v]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
    return components

g = {
    1:[2], 2:[1,3], 3:[2],
    4:[5], 5:[4],
    6:[]
}
print(count_components(g))