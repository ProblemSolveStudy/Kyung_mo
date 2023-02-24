import sys

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()
result = 0
idx = 1
for i in arr:
    result += abs(i-idx)
    idx+=1
print(result)