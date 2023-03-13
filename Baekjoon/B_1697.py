import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
graph = [0] * (k+1)
visited = [0] * 100001
def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for nx in (x-1, x+1, 2*x):
            if 0<=nx<=100000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(bfs(n))