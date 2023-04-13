import sys

# 바텀 업
n = int(sys.stdin.readline())
dp = [0] * (n+1)

# dp[0] = 0
# dp[1] = 1

# for i in range(2, n+1):
#     dp[i] = dp[i-2] + dp[i-1]

# print(dp)


# 탑 다운
def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if dp[x] != 0:
        return dp[x]

    dp[x] = fibo(x-1)+fibo(x-2)
    return dp[x]

print(fibo(n))
