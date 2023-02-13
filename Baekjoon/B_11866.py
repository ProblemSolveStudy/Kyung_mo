import sys
from collections import deque

n,k = map(int, sys.stdin.readline().rstrip().split())
table = deque([i for i in range(1, n+1)])
remove = []
while table:
    table.rotate(-(k-1))
    remove.append(table.popleft())

print(f'<{", ".join(map(str, remove))}>')