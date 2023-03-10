import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [0] * (n+1)
    queue = deque([start])
    visited[start] = 1
    while queue:
        target = queue.popleft()
        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                queue.append(i)
    return sum(visited)
result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result)) + 1)