import sys, copy
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1 ,0 ,0]
dy = [0, 0 , -1, 1]

def bfs(graph, i, j, water):
    if graph[i][j] <= water:
        return False
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] <= water:
                continue
            if graph[nx][ny] > water:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return True

result = []
for water in range(1, 101):
    g = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if bfs(g, i, j, water):
                cnt += 1
    
    result.append(cnt)

print(max(result))