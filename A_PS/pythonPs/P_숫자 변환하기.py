from collections import deque
answer = 0
visited = [0] * 1000001
def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == y:
            return visited[x]
        for nx in (x+n, x*2, x*3):
            if 0<=nx<=1000000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

x,y,n = 10, 40, 5

print(bfs(x))