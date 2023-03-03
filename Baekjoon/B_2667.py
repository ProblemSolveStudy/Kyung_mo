from collections import deque
import sys
def bfs(graph,x,y):
    cnt = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt


dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i,j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])