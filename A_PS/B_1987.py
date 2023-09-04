import sys
from collections import deque
a,b = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(a)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 1
def bfs(x,y):
    q = set([(x,y, graph[0][0])])
    global cnt
    while q:
        x,y,commands = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx<a and 0<=ny<b and graph[nx][ny] not in commands:
                q.add((nx,ny, commands + graph[nx][ny]))
                cnt = max(cnt, len(commands) + 1)

bfs(0,0)
print(cnt)