# 1. T 걸리는 시간, P 받는 금액
# 2. 최대 금액을 받을 수 있도록 하자!
# 3. N일 동안 최대한 많은 상담을 진행하도록 할 것이며 , 그러면서 최대 금액을 받아야 한다.
# 4. 최대 상담일자가 N일을 넘어가면 안된다.
# 5. 각 날짜를 할것인지 말것인지를 정해야 할듯함
# arr [[a,b]] a : 날짜 b: 금액
import sys
n = int(sys.stdin.readline())
dp=[0] * (n+1)
arr = [[0,0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1]) # dp 최대값 (전)
    finish = i + arr[i][0] - 1
    if finish > n:
        continue
    dp[finish] = max(dp[i-1] + arr[i][1], dp[finish])

print(max(dp))