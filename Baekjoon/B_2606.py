from collections import deque
import sys

def bfs(graph, start, visited):
    cnt = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                cnt += 1    
                visited[i] = True
    return cnt

computer = int(sys.stdin.readline())
n = int(sys.stdin.readline())

graph = [[] for _ in range(computer + 1)]
visited = [False] * (computer + 1)

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

print(bfs(graph, 1, visited))