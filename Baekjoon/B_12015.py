import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())

# [10, 10, 20, 20, 30, 50]
arr = list(map(int, input().rstrip().split()))
arr.sort()
print(arr)

newArr = [arr[0]]


for i in arr:
    if i > newArr[-1]:
        newArr.append(i)
    else:
        newArr[bisect_left(newArr, i)] = i
        print(bisect_left(newArr, i))

print(len(newArr))