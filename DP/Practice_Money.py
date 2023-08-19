import sys
n,m = map(int, input().split())
money = [int(input()) for _ in range(n)]

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = 