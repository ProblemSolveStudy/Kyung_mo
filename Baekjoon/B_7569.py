# 1 익은 토마토
# 0 익지 않은 토마토
# -1 토마토가 없는 칸
# n개의 줄이 h번 반복되어 주어진다?

import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())

# 앞, 뒤, 상(현재 위치 - n), 하(현재 위치 + n), 좌, 우

graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

res = 0

def bfs():    
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    queue.append((nz,nx,ny))


for i in range(h): # 높이
    for j in range(n): # 행
        for k in range(m): # 열
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        res = max(res, max(j))
print(res - 1)