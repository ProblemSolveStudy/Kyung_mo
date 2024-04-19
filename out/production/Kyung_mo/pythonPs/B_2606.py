# dfs로 풀 수 있을 것 같아
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

computer = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(1, m+1):
    a,b = map(int,sys.stdin.readline().split())
    computer[a].append(b)
    computer[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    global cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
    return cnt-1

print(dfs(computer, 1, visited))