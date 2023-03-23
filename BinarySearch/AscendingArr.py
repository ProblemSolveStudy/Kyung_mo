import sys
from bisect import bisect_right, bisect_left

def count_by_range(array, left, right):
    right_index = bisect_right(array, right)
    left_index = bisect_left(array, left)
    return right_index - left_index

n,x = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

count = count_by_range(arr, x, x)
if count == 0:
    print(-1)
else:
    print(count)