import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

start = 1
end = max(arr)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if mid >= x:
            total += x
        else:
            total += mid
    
    if total <= budget:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)