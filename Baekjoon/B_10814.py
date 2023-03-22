import sys
n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip().split()) for _ in range(n)]

arr.sort(key=lambda x : int(x[0]))
for i in range(len(arr)):
    print(*arr[i])