# 행렬 곱셈의 조건은 행렬 A와 B를 곱하게 되면, A의 열의 개수와 B의 행의 개수가 같아야 한다.
# 곱셈 연산의 경우 A*B = A'Row * B'Col * B'Row(A'Col)
# 예제 입력의 경우 AB = (5 * 2 * 3) + (AB)C = (5 * 6 * 2) = 90
# 행렬 두개 곱하면 가운데 껴잇는게 없어지는 형식임
# 답지이해 불가 죄송 ㅠㅠㅠㅠ

import sys
INF = 2**32 - 1
n = int(sys.stdin.readline())
r = []
c = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    r.append(a)
    c.append(b)


def func(x,y):
    if(dp[x][y] > 0):
        return dp[x][y]
    if y-x<=0:
        return 0
    mm = INF
    for k in range(x, y):
        mm = min(mm, func(x,k) + func(k+1, y) + r[x] * c[k] * c[y])
    dp[x][y] = mm
    return mm

print(func(0, n-1))