import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort(reverse=True)
level=arr[0]
gold=0
for i in range(1,len(arr)):
    gold += level + arr[i]

print(gold)
