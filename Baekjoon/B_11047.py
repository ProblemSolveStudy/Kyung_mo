import sys
n,k = map(int, sys.stdin.readline().split())

coin = []

for i in range(n):
    coin.append(int(sys.stdin.readline()))

coin.reverse()
result = 0
for i in coin:
    result += k // i
    k %= i

print(result)