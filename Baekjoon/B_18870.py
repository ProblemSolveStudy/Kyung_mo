import sys
import copy
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr_copy = copy.deepcopy(arr)

arr_copy = list(set(arr_copy))
arr_copy.sort()

for i in arr:
    print(arr_copy.index(i), end=' ')