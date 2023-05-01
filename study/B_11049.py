# 행렬 곱셈의 조건은 행렬 A와 B를 곱하게 되면, A의 열의 개수와 B의 행의 개수가 같아야 한다.
# 곱셈 연산의 경우 A*B = A'Row * B'Col * B'Row(A'Col)
# 예제 입력의 경우 AB = (5 * 2 * 3) + (AB)C = (5 * 6 * 2) = 90
# 

import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
dp = [0] * (len(arr) + 1)

for i in range(len(arr)):
    