# 아기상어의 초반크기는 2
# 1초에 상화좌우로 인접한 칸 하나씩을 방문할 수 있음
# 아기상어는 자기보다 작은애만 먹을 수 있음 (크기가 같으면 못먹음)
# 대신 크기가 같으면 지나가기는 가능함
# 크기가 2인 아기상어가 물고기를 2마리 먹으면 크기가 3으로 진화함

# 물고기가 공간에 없다면 엄마 상어에게 도움을 요청 (프로그램 종료)
# 먹을 수 있는 물고기가 많다면, 가장 가까운 친구부터 먹으면서 다닌다.
# 가장 위의 물고기 -> 그다음엔 왼쪽!

# bfs활용으로 너비탐색으로 해야할 듯

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dx, dy = [-1, 1, 0 , 0], [0, 0, -1, 1]
start = 9
shark_size = 2
shark_now_eat = 0
x,y = 0, 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x,y = i, j
            graph[i][j] = 0

def bfs(x,y):
    queue = deque([(x,y)])
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if shark_size >= graph[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited

def solve(visited):
    x,y = 0,0
    min_distance = 1e9
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and 1<=graph[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x,y = i,j
    
    if min_distance == 1e9:
        return False
    else:
        return x,y,min_distance
                

answer = 0
food = 0

while True:
    result = solve(bfs(x,y))

    if not result:
        print(answer)
        break
    else:
        x,y = result[0], result[1]
        answer += result[2]
        graph[x][y] = 0
        food += 1

    if food >= shark_size:
        shark_size += 1
        food = 0
