import sys
n,m = map(int, sys.stdin.readline().split())
amount = [int(sys.stdin.readline()) for _ in range(n)]

start = 1
end = sum(amount)
result = 0
while (start <= end):
    cnt = 1
    mid = (start + end) // 2
    now = mid
    for x in amount:
        if now - x < 0:
            cnt += 1
            now = mid
        now -= x
    
    if cnt > m or mid < max(amount):
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)