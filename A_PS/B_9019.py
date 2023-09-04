import sys
from collections import deque
def D(n):
    return (2*n) % 10000, "D"
def S(n):
    return (n-1) % 10000, "S"
def L(n):
    return (n*10 + (n//1000)) % 10000, "L"
def R(n):
    return (n//10 + (n%10)*1000) % 10000, "R"

def bfs(start, visited):
    q = deque([(start, "")])
    while q:
        s, commands = q.popleft()
        if s == b:
            return commands
        for nx, command in (D(s), S(s), R(s), L(s)):
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, commands + command))

for _ in range(int(sys.stdin.readline())):
    visited = [False] * 10000
    a,b = map(int, sys.stdin.readline().split())
    print(bfs(a, visited))