import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

start = 0
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for a in arr:
        if a >= mid:
            total += mid
        else:
            total += a
    
    if total > budget: # 사용량이 예산보다 크다면??? mid를 줄여야지
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)