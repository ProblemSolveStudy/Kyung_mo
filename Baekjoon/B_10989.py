import sys

n = int(sys.stdin.readline())
numList = [0] * 10001

for _ in range(n):
    numList[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numList[i] != 0:
        for j in range(numList[i]):
            print(i)