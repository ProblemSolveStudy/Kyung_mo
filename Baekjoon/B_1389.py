import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited = [0] * (n+1)
    visited[start] = 1
    while q:
        s = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[s] + 1

    return sum(visited)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result)) + 1)