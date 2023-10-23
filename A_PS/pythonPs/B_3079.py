import sys
n,m = map(int, sys.stdin.readline().split())
time = [int(sys.stdin.readline()) for _ in range(n)]

start = min(time)
end = max(time) * m
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in time:
        total += mid // i
    if total >= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)