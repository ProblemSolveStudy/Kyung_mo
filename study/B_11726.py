import sys

# 하다보니 규칙이생겨서;;;;;;

dp = [0] * 1001

n = int(sys.stdin.readline())

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n] % 10007)