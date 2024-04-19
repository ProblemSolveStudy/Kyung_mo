import sys

n,k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

start = 1
end = sum(arr)
result = 0
while (start <= end):
    cnt = 1
    mid = (start + end) // 2
    now = mid

    for x in arr:
        if now - x < 0:
            cnt += 1
            now = mid
        now -= x
    
    if cnt > k or mid < max(arr):
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)