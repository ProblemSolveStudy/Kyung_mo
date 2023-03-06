import sys

def dfs(v, cnt):
    visited[v] = True
    cnt += 1

    if v == target:
        result.append(cnt)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt)
    
n = int(sys.stdin.readline())
start, target = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

dfs(start, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)