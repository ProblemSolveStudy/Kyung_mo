import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
a = list(set(arr))
a.sort()
dict = {}
for i in range(len(a)):
    dict[a[i]] = i

for i in arr:
    print(dict[i], end=' ')