import sys

input = sys.stdin.readline
n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start = 0
end = max(arr) * m
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for i in arr:
        total += mid//i
    
    if total >= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)