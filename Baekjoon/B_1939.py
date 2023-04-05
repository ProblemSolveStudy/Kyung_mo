import sys
from collections import deque

def bfs(weigth):
    visited = [False] * (n+1)
    q = deque()
    q.append(first)
    visited[first] = True

    while q:
        x = q.popleft()
        for v, w in bridges[x]:
            if not visited[v] and w >= weigth:
                visited[v] = True
                q.append(v)
    
    if visited[second]: return True
    else: return False

n,m = map(int, sys.stdin.readline().split())
bridges = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    bridges[a].append([b,c])
    bridges[b].append([a,c])
first, second = map(int ,sys.stdin.readline().split())

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