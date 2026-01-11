# week_hw4.py

print('1-2--------------')
def squared(n):
    for i in range(1,n+1) :
        yield i ** 2
sq = squared(10)
for i in sq:
    print(i)

print('2-1--------------')
class Stack:
    def __init__(self):
        self.stack = ['두산','로키','부트']
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return
    
    def stauts_stack(self):
        return self.stack
s = Stack()
s.push('캠프')
print(s.stauts_stack())

print('2-2--------------')
s.pop()
print(s.stauts_stack())

print('3-1--------------')
MyGraph={
    '두':['산','로','키'],
    '산':['두','부'],
    '로':['두'],
    '키':['두','트'],
    '부':['산'],
    '트':['키','캠','프'],
    '캠':['트'],
    '프':['트']
}
def my_dfs(graph, start_node):
    stack=list()
    visited=list()
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            stack.extend(reversed(graph[node]))
            visited.append(node)
    print(f'dfs - {visited}')
    print(f'6번째로 출력된 데이터: {visited[5]}')
    return visited

my_dfs(MyGraph,'두')

print('3-2--------------')
MyGraph={
    '두':['산','로','키'],
    '산':['두','부'],
    '로':['두'],
    '키':['두','트'],
    '부':['산'],
    '트':['키','캠','프'],
    '캠':['트'],
    '프':['트']
}
def my_bfs(graph, start_node):
    queue=list()
    visited=list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
    print(f'bfs - {visited}')
    print(f'6번째로 출력된 데이터: {visited[5]}')
    return visited

my_bfs(MyGraph, '두')

print('4-1--------------')
import pandas as pd
path = r'D:\rokey\python\week\data1.csv'
car = pd.read_csv(path)
print(car)

print('4-2--------------')
import matplotlib.pyplot as plt
x=[2016,2017,2018,2019,2020,2021,2022,2023,2024]
y=[1293,1304,1397,1424,659,879,1058,1196,1143]
plt.plot(x,y)
plt.xlabel('year')
plt.ylabel('impounded vehicles')
plt.title('Annual number of impounded vehicles')
plt.show()

