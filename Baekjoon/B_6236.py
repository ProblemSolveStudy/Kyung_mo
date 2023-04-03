# m번만큼 빼낼 수 있는 k원의 최소값을 구해야 함

import sys
n,m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

start = min(arr)
end = sum(arr)

result = 0

while start <= end:
    mid = (start+end)//2
    money = mid
    total = 1
    
    for x in arr:
        if money - x<0:
            money = mid
            total += 1
        money -= x

    if total > m or mid < max(arr):
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)
