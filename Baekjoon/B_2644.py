import sys

n = int(sys.stdin.readline())
target1, target2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
result = []
def dfs(v, visited, cnt):
    visited[v] = True
    cnt += 1
    if v == target2:
        result.append(cnt)
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, cnt)

dfs(target1, visited, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)