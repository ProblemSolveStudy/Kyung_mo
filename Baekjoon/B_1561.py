import sys
input = sys.stdin.readline

# 아이들을 모두 태울 값이 mid
# 아이들 n, 놀이기구 개수 m
n,m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr) * m
result = 0

if n < m:
    print(n)
else:
    start = 0
    end = max(arr) * m
    while start <= end:
        total = m
        mid = (start + end) // 2
        
        for i in arr:
            total += mid // i
        if total >= n:
            end = mid - 1
            result = mid
        else:
            start = mid + 1
    
    total = m
    for i in range(m):
        total += (result - 1) // arr[i]
    
    for i in range(m):
        if result % arr[i] == 0:
            total += 1
        if total == n:
            print(i+1)
            break

    print(result)