from collections import deque
import sys

n,k = map(int, sys.stdin.readline().split())
max = 100000
visited = [0] * (max + 1)

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        x = q.popleft()
        if x == k:
            return visited[x] - 1
        for nx in (x-1, x+1, 2*x):
            if 0<=nx<max and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

print(bfs(n))
            