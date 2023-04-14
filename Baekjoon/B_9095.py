import sys

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    print(dp[n])
