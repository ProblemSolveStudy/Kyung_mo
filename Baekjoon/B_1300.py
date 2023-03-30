import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = n*n
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(1, n+1):
        total += min(mid // i, n)
    
    if total < k: 
        start = mid + 1
    else:
        result = mid # 최소 mid 값을 찾기
        end = mid - 1
print(result)