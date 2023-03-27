import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

start = 1
end = N*N

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(1, N+1):
        total += min(mid//i, N)

    if total >= K:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)