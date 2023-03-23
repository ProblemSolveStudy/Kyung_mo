# 메모리제한이 8MB이기 때문에 최소한으로 줄여야만 한다

import sys

n = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(n):
    a = int(sys.stdin.readline())
    count[a] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)