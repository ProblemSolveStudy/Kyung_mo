import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(sys.stdin.readline())
target_arr = list(map(int, sys.stdin.readline().split()))


def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return arr[start:end+1].count(array[mid])
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)

numdict = {}

for target in arr:
    start = 0
    end = N-1
    if target not in numdict:
        numdict[target] = binary_search(arr, target, start, end)

print(' '.join(str(numdict[x]) if x in numdict else '0' for x in target_arr))