import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = list(map(int, input().rstrip().split()))

arr.sort()

dist = [arr[i] - arr[i-1] for i in range(1, len(arr))]

dist.sort(reverse=True)

result = 0
for i in range(k-1, len(dist)):
    result += dist[i]
print(result)