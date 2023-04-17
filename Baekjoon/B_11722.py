import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# arr을 순회하면서 dp에는 순열 개수를 memorization한다.
# 