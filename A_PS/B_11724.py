import sys
sys.setrecursionlimit(10**9)
n,m = map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)
cnt = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)