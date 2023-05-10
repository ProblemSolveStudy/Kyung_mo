from collections import deque
import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for i in range(m):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# def bfs(start):
#     q = deque([start])
#     visited = [0] * (n+1)
#     visited[start] = 1
#     while q:
#         s = q.popleft()
#         for i in graph[s]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = visited[s] + 1
    
#     return sum(visited)

# result = []
# for i in range(1, n):
#     result.append(bfs(i))

# print(result.index(min(result)) + 1)

n,m = map(int, sys.stdin.readline().split())
INF = 1e9
graph = [[INF] * (n+1) for _ in range(n+1)]

# 직접 친구면 1
# 해당 문제에서는 간선에대한 비용이 전부 1임
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1): # 거쳐가는 노드
    graph[k][k] = 0 
    for i in range(1, n+1): # 출발 노드
        for j in range(1, n+1): # 도착 노드
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # 플로이드워셜 점화식

min_count = answer = INF
for i in range(1, n+1):
    print(graph[i][1:])
    count = sum(graph[i][1:])
    if count < min_count:
        min_count = count
        answer = i

print(answer)