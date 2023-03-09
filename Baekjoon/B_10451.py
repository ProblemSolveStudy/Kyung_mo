import sys

def dfs(graph, v, visited):
    visited[v] = True
    next = graph[v]
    if not visited[next]:
        dfs(graph,next,visited)
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [True] + [False] * (n)
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1

    print(cnt)