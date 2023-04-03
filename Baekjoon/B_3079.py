import sys

n,m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

start = 0
end = max(arr) * m
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(n):
        total += mid // arr[i]
    
    if total >= m:
        end = mid-1
        result = mid
    else:
        start = mid + 1

print(result)