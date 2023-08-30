import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())

result = []
max = 100001
visited = [0] * (max)
def bfs(start):
    q = deque([start])
    while q:
        s = q.popleft()
        if s == k:
            return visited[s]
        for nx in (s-1, s+1, 2*s):
            if 0<=nx<max and not visited[nx]:
                visited[nx] = visited[s] + 1
                q.append(nx)

print(bfs(n))