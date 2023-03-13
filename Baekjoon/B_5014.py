import sys
from collections import deque
max = 1000000
f,s,g,u,d = map(int, sys.stdin.readline().split())
visited = [0] * (f+1)
def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        s = queue.popleft()
        if s == g:
            return visited[s] - 1
        for ns in (s+u, s-d):
            if 1<=ns<=f and not visited[ns] :
                visited[ns] = visited[s] + 1
                queue.append(ns)
    return "use the stairs"

print(bfs(s))