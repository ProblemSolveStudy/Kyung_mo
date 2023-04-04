# total값을 어떻게 잡느냐가 관건임
# total은 하나당 진행하는 사람의 수?

import sys
n,m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

start = 1
end = max(arr) * m
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for x in arr:
        total += mid//x
    
    if total >= m:
        result = mid
        end = mid-1
    else:
        start = mid+1

print(result)