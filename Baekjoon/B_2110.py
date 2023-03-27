import sys
input = sys.stdin.readline

n,c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start = 0
end = max(arr)

result = 0
while (start<= end):
    total = 1
    mid = (start+end)//2
    current = arr[0]

    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            total += 1
            current = arr[i]
    
    if total < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)