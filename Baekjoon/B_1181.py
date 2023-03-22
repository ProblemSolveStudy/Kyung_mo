import sys
n = int(sys.stdin.readline())

arr = [sys.stdin.readline().rstrip() for _ in range(n)]
arr = list(set(arr))
arr.sort()
arr.sort(key=lambda x: len(x))


for i in range(len(arr)):
    print("".join(arr[i]))