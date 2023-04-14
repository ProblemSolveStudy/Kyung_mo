# 마지막 계단은 밟아야 하지만, 첫 계단은 밟아도 된다는 조건은 없음
import sys

t = int(sys.stdin.readline())
score = [0] * 301
for i in range(1, t+1):
    score[i] = int(sys.stdin.readline())
dp = [0] * 301
dp[0] = score[0]
dp[1] = score[1]
dp[2] = max(score[1] + score[2], score[2])
dp[3] = max(score[1] + score[3], score[2] + score[3])

for i in range(4, t+1):
    dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])

print(dp[t])