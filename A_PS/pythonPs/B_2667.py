import sys
from collections import deque

n = int(sys.stdin.readline())
graph=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

house_cnt = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque([])
    q.append((x,y))
    cnt = 1
    graph[x][y] += 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                cnt += 1
                q.append((nx,ny))
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_cnt.append(bfs(i,j))

print(len(house_cnt))
house_cnt.sort()
for i in range(len(house_cnt)):
    print(house_cnt[i])