import sys
from collections import deque
m,n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1 ,0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    q = deque(start)
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx >= n or ny<0 or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    
    if any(0 in l for l in graph) or all(0 in l for l in graph):
        return -1
    return max(map(max, graph)) - 1
tmt = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tmt.append([i,j])

print(bfs(tmt))
print(graph)