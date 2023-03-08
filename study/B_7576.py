# 전부 익어있다면 0
# 전부 익을 수 없다면 -1
# 시간 복잡도 O(n^3)
# 메모리 154836KB, 시간 1608ms


import sys
from collections import deque

# n : 행, m : 열
m,n = map(int, sys.stdin.readline().split()) # 행렬 값 받아오기
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)] # 2차원배열로 그래프 받아오기
dx = [-1, 1, 0 ,0] # 움직일 수 있는 방향
dy = [0, 0, -1, 1]

def bfs(lst): # 예제 3으로 보면 lst안에 값으로 [0,0], [3,5]가 들어오게 됨
    queue = deque() 
    for tomato in lst: # 처음에 익은 토마토가 여러개일 경우에 리스트로 받아서 큐에 넣어줌
        queue.append(tomato)

    
    while queue: 
        for _ in range(len(queue)): # queue의 개수만큼 돌리기 때문에 동시에 bfs 실행이 가능해짐
            # 이후부터는 queue에 들어간 익은 복숭아들이 순차적으로 동시에 실행되는 듯한 느낌으로 번갈아가며 실행 가능
            x,y = queue.popleft()
            # 일반적인 방향 탐색 방법
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] == -1:
                    continue
                if graph[nx][ny] == 0:
                    # graph에서 max값을 반환하기 위해서 +1 증가
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

        # 만약 graph안에 0이 하나라도 있거나
        # 전부 0일 경우엔 -1반환
    if any(0 in l for l in graph) or all(0 in l for l in graph): 
        return -1
    # 그래프 내에서 한칸 이동시마다 +1을 해주기 때문에
    return max(map(max, graph)) - 1 
    # 그래프에서 가장 max값을 반환

tmt = []

# 익은 토마토가 여러개일 경우에는 bfs가 동시출발해야 함
# 2중 for문 돌면서 graph에서 시작시에 1(익은토마토)인 리스트 생성
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
           tmt.append([i,j])
        
print(bfs(tmt))


# 답지 버전
# 시간 복잡도 O(n^2)
# 메모리 98528 KB, 시간 1400ms
answer_m, answer_n = map(int, sys.stdin.readline().split())
answer_graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(answer_n)]
answer_queue = deque([])

dx = [-1, 1, 0 ,0] # 움직일 수 있는 방향
dy = [0, 0, -1, 1]

res = 0

for i in range(answer_n):
    for j in range(answer_m):
        if answer_graph[i][j] == 1:
            answer_queue.append([i,j])

def bfs():
    while answer_queue:
        x,y = answer_queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i] , y+dy[i]
            if 0 <= nx < answer_n and 0<=ny<answer_m and answer_graph[nx][ny] == 0:
                answer_graph[nx][ny] = answer_graph[x][y] + 1
                answer_queue.append((nx, ny))

bfs()
for i in answer_graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    
    res = max(res, max(i))
print(res - 1)