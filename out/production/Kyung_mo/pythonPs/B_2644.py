import sys
input = sys.stdin.readline

n = int(input())
first, second = map(int, input().split())
m = int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
result = []
def dfs(start, cnt, visited):
    visited[start] = True
    cnt += 1
    if start == second:
        result.append(cnt)
    for i in graph[start]:
        if not visited[i]:
            dfs(i, cnt, visited)
dfs(first, 0, visited)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)