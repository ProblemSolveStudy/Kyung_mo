import sys
input = sys.stdin.readline

n,m = map(int, input().split())
time = list(map(int, input().split()))

if n<m:
    print(n)
else:
    start = 0
    end = max(time) * n
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = m
        
        for t in time:
            total += mid // t
        
        if total >= n:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    cnt = m

    for t in time:
        cnt += (result - 1) // t

    for i in range(m):
        if result % time[i] == 0:
            cnt += 1
        if cnt == n:
            print(i + 1)
            break
