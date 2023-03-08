import sys, copy
from collections import deque

def bfs(graph,x,y,depth):
    if graph[x][y] <= depth:
        return False
    
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if nx < 0 or nx>=n or ny < 0 or ny>=n:
                continue
            
            if graph[nx][ny] > depth:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return True

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
result = []
for depth in range(101):
    cnt=0
    g = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if bfs(g,i,j,depth):
                cnt+=1
                
    result.append(cnt)

print(max(result))