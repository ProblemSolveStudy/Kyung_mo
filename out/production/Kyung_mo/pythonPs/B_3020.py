import sys
n,h = map(int, sys.stdin.readline().split())
mite, tite = [], []

for i in range(n//2):
    mite.append(int(sys.stdin.readline()))
    tite.append(h-int(sys.stdin.readline()))

mite.sort()
tite.sort()

min_num, result = n, 0

def binarySearch(start ,end, arr, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

for i in range(1, h+1):
    r1 = n//2 - binarySearch(0, n//2, mite, i-1)
    r2 = binarySearch(0, n//2, tite, i-1)
    total = r1 + r2
    if min_num == total:
        result += 1
    elif min_num > total:
        min_num = total
        result = 1

print(min_num, result)