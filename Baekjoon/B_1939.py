import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
first, second = map(int, input().split())

def bfs(weight):
    visited = [False] * (n+1)
    q = deque()
    q.append(first)
    visited[first] = True
    while q:
        x = q.popleft()
        for i,w in graph[x]:
            if visited[i] == False and weight <= w:
                visited[i] = True
                q.append(i)
    if visited[second] == True: return True
    else: return False

start = 0
end = 1000000000
result = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
