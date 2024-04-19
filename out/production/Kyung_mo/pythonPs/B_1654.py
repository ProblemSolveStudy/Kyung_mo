import sys
k,n = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(lines)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in lines:
        if x >= mid:
            total += x // mid
    if total < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)