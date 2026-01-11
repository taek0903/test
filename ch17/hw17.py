print('7-------------------')
from pprint import pprint
map1 = [
    [0,1,1,1,1,1],
    [0,1,0,0,0,1],
    [0,1,0,1,0,1],
    [0,1,0,1,0,0],
    [0,0,0,1,1,0],
    [1,1,1,1,1,0]
]
pprint(map1)

print('8-------------------')
def build_map(rows, cols, grid):
    if len(grid) !=rows:
        raise ValueError
    for row in grid:
        if len(row) != cols:
            raise ValueError
    return grid

map2 = build_map(6,6,map1)
pprint(map2)

print('9-------------------')
rows=len(map1)
cols=len(map1[0])
def navigate(x,y):
    if not (0 <= x <rows and 0 <= y <cols):         # x,y값이 범위를 벗어나면 예외 처리
        return False
    if map1[x][y] != 0:                             # map1[x][y]의 값이 길이 아니면 예외 처리
        return False
    
    stack = [(x,y)]                                 # x,y 튜플을 스택값에 추가
    map1[x][y] = 2                                  # 지나간 길을 처리 2로 하는 이유는 길의 값은 0 벽의 값은 1이기 때문에

    while stack:
        x,y=stack.pop()                             # 스택에서 빼낸 (x,y)값
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:  # 상하좌우 리스트 반복
            nx, ny = x+ dx, y+dy                    # 상화좌우 더해주기

            if 0 <= nx < rows and 0 <= ny < cols and map1[nx][ny] == 0:     # 범위를 만족하고 값이 0일경우 동작
                map1[nx][ny]=2                      # 리스트 값을 2로 변환
                stack.append((nx,ny))               # 변환한 값의 자표를 스택에 집어 넣기
        print(f'stack: {stack}')
        print("이동경로확인-----------")
        for r in map1:
            print(r)
    return True
print(navigate(0,0))

print('10------------------')
map1 = [
    [0,1,1,1,1,1],
    [0,1,0,0,0,1],
    [0,1,0,1,0,1],
    [0,1,0,1,0,0],
    [0,0,0,1,1,0],
    [1,1,1,1,1,0]
]
rows=len(map1)
cols=len(map1[0])
def navigate_bfs(x,y):
    if not (0 <= x <rows and 0 <= y < cols):
        return False
    if map1[x][y] != 0:
        return False
    
    queue = [(x,y)]
    head=0
    map1[x][y] = 2

    while head < len(queue):
        x, y =queue[head]
        head += 1
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
        
            if 0<=nx <rows and 0 <= ny <cols and map1[nx][ny] == 0:
                map1[nx][ny]=2
                queue.append((nx,ny))
        print(f'queue: {queue}')
        print("이동경로확인-----------")
        for r in map1:
            print(r)
    return True
print(navigate_bfs(0,0))