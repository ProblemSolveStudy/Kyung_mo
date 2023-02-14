import sys

n, k = map(int, sys.stdin.readline().split())

coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

coin.reverse()

cnt = 0

for i in coin:
    cnt += k // i
    k %= i
print(cnt)