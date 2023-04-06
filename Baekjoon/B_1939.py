import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
bridges = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    bridges[a].append([b,c])
    bridges[b].append([a,c])
first,second = map(int, sys.stdin.readline().split())

def bfs(weight):
    visited = [False] * (n+1)
    q = deque()
    q.append(first)
    visited[first] = True

    while q:
        x = q.popleft()
        for i,w in bridges[x]:
            if visited[i] == False and w>=weight:
                visited[i] = True
                q.append(i)
    if visited[second]: return True # 방문이 되는 경로임
    else: return False # 방문이 불가능한 경로임

start = 0
end = 1000000000
result = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)