import sys
from collections import deque

# sys.setrecursionlimit(10**9)
n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [True] + [False] * (n)
cnt=0

# def dfs(graph, v, visited):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)

def bfs(start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# for i in range(1,n+1):
#     if not visited[i]:
#         dfs(graph, i, visited)
#         cnt += 1

for i in range(1, n+1):
    if not visited[i]:
        bfs(i, visited)
        cnt+=1
        
print(cnt)