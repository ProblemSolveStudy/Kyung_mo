# mid와 total을 잘 생각할 것
import sys

n,m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

start = 1
end = sum(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    money = mid
    total = 1

    for x in arr:
        if money - x < 0:
            total += 1
            money = mid
        money -= x
    
    if total > m or mid < max(arr):
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)