import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
visited = [0] * (100001)

def bfs(start):
    q = deque([start])
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        for nx in (x-1, x+1, 2*x):
            if 0<=nx<100000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

print(bfs(n))