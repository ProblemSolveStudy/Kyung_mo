# 항상 내리막길이여야한다!
# 결국 dfs를 활용해야 하고, 재귀를 쓰면서 이미 방문한곳이라면 굳이 처음부터 시작할 필요가 없다는 것
# visited = dp라고 생각하면 결국 dfs문제랑 다를게 없음
# 2번째 줄 조건만 추가하면 될 것 같음
# x = row y = column
# 시간초과가 발생하는데?

# import sys

# def dfs(x,y):
#     if x == m-1 and y == n-1:
#         return 1

#     if dp[x][y] != -1:
#         return dp[x][y]

#     cnt = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0<=nx<m and 0<=ny<n and arr[nx][ny] < arr[x][y]:
#             cnt += dfs(nx,ny)
#     dp[x][y] = cnt
#     print(dp)
#     return dp[x][y]


# m,n = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# dp = [[-1 for _ in range(n)] for _ in range(m)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# print(dfs(0,0))

## 04/25 문제 재풀이
import sys
m,n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx,dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<m and 0<=ny<n and graph[nx][ny] < graph[x][y]:
            cnt += dfs(nx, ny)
    dp[x][y] = cnt
    return dp[x][y]

print(dfs(0,0))