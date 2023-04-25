# 각 장이 쓰여진 파일을 합쳐서 최종적으로 한개의 파일을 만듬
# 두 개의 파일을 합칠 때 필요한 비용 = 두 파일 크기의 합 (점화식 사용)
# 경우의수를 dp에 저장할 것
# 연속되게 합쳐나가야 한다.

# 첫번째 파일이 가능한 경우의 수
# 40+30, 

import sys
k = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (k+1)
dp[1] = min(arr[1]+arr[2], arr[1] + arr[2] + arr[3])
for i in range(2, k):
    dp[i] = min(arr[i] + arr[i+1], dp[i] + arr[i+1])
print(dp)