# p2.py
maze = [
    [1,1,0,1,0],
    [0,1,0,1,1],
    [1,1,0,0,1],
    [1,0,1,1,1],
    [1,1,1,0,0]
]

ice_case = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
print(maze)
rows=len(ice_case)
cols=len(ice_case[0])

def count_ice(x,y):
    start_node=(x,y)
    stack = [start_node]

    # 스택이 비워지면 얼음 하나 확인
    while stack:
        x,y = stack.pop()
        
        # 주어진 범위를 벗어나는 경우 무시
        if x<0 or x>=rows or y<0 or y>=cols:
            continue
        # 현재 노드를 아직 방문하지 않았더라면
        if ice_case[x][y] == 0:
            
            # 방문처리
            ice_case[x][y] = 1
            
            # 인접 노드를 스택 추가
            stack.append((x-1, y))    # 좌노드
            stack.append((x+1, y))    # 우노드
            stack.append((x, y-1))    # 하노드
            stack.append((x, y+1))    # 상노드

            print(stack)            # 노드 좌표

            print(f'이동 경로 확인 ------------')
            for i in ice_case:
                print(i)
    
    # 얼음 확인 여부 반환
    return True

result=0
for i in range(0,rows):
    for j in range(0,cols):
        # 한번 얼음 개수로 카운트된 얼음은 다시 카운트 되면 안됨
        if ice_case[i][j] == 0:
            if count_ice(i,j) == True:
                result += 1
print(f'얼음개수: {result}')