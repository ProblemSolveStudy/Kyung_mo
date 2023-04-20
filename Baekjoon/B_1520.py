# 항상 내리막길이여야한다!
# 결국 dfs를 활용해야 하고, 재귀를 쓰면서 이미 방문한곳이라면 굳이 처음부터 시작할 필요가 없다는 것
# visited = dp라고 생각하면 결국 dfs문제랑 다를게 없음
# 2번째 줄 조건만 추가하면 될 것 같음
# x = row y = column

import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x,y):

    if x == m-1 and y == n-1:
        return 1
    
    if visited[x][y] != 0:
        return visited[x][y]

    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            cnt += dfs(nx, ny)
    
    visited[x][y] = cnt
    print(visited)
    return visited[x][y]


print(dfs(0,0))