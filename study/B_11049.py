# 행렬 곱셈의 조건은 행렬 A와 B를 곱하게 되면, A의 열의 개수와 B의 행의 개수가 같아야 한다.
# 곱셈 연산의 경우 A*B = A'Row * B'Col * B'Row(A'Col)
# 예제 입력의 경우 AB = (5 * 2 * 3) + (AB)C = (5 * 6 * 2) = 90
# 

import sys
input = sys.stdin.readline

n = int(input())
r = [0]
c = [0]
dp = [0] * (n+1)
arr = [[0,0]]+[list(map(int, input().split())) for _ in range(n)]

def arrMul(arr1, arr2):
    return arr1[0] * arr2[1] * arr2[0]

for i in range(1, n+1):
    dp[i] = 