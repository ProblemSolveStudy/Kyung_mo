import sys
# from bisect import bisect_left

# n = int(sys.stdin.readline())
# arr = list(map(lambda x: int(x) * -1, sys.stdin.readline().split()))

# dp = [arr[0]]

# for i in range(n):
#     if arr[i] > dp[-1]:
#         dp.append(arr[i])
#     else:
#         idx = bisect_left(dp, arr[i])
#         dp[idx] = arr[i]

# print(len(dp))

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))