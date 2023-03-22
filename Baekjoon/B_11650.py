import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

arr.sort()
for i in range(len(arr)):
    print(*arr[i])