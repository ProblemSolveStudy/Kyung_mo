import sys, copy
from collections import deque
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
result = []
dx, dy = [-1, 1, 0 ,0], [0, 0, -1, 1]


def bfs(graph, x, y, depth):
    if graph[x][y] <= depth:
        return False
    
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < n and graph[nx][ny] > depth:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    
    return True

for depth in range(101):
    g = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if bfs(g, i, j, depth):
                cnt += 1
    
    result.append(cnt)

print(max(result))