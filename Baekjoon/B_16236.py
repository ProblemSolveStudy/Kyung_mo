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

def bfs(x, y):
    shark_size = 2
    shark_now_eat = 0
    cnt = 0
    queue = deque([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] > shark_size: # 아기상어보다 크면 넘어가;;;
                continue
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 그래프 넘어가면 넘어가 ;;
                continue
            if graph[nx][ny] < shark_size: # 먹을 수 있는애면 먹어!
                shark_now_eat += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
            elif graph[nx][ny] == shark_size:
                queue.append((nx, ny))
                cnt += 1

    return True
                



for i in range(n):
    for j in range(n):
        if graph[i][j] == start:
            bfs()