import sys
from collections import deque

# n : 정점 m : 간선 v: 탐색 시작 점
n,m,v = map(int, sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]
visited=[False] * (n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

for i in range(len(graph)):
    graph[i].sort()

dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph,v,visited)