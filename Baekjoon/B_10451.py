import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    next = graph[start]
    if not visited[next]:
        dfs(graph, next, visited)
t = int(input())


for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().rstrip().split()))
    visited = [True] + [False] * (n)
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt+=1
    print(cnt)