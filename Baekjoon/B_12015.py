import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for a in arr:
    if dp[-1] < a:
        dp.append(a)
    else:
        dp[bisect_left(dp,a)] = a

print(len(dp) - 1)


import sys
input = sys.stdin.readline

n = int(input()) # 수열의 길이를 입력받는다.
cases = list(map(int, input().split())) # 수열을 리스트로 받아온다.
lis = [0] # LIS(최장 증가 부분 수열)을 담을 리스트를 초기화한다.

for case in cases: # 수열을 하나씩 순회한다.
    if lis[-1] < case: # LIS의 마지막 값보다 큰 경우,
        lis.append(case) # LIS에 추가한다.
    else: # LIS의 마지막 값보다 작거나 같은 경우,
        left = 0 # LIS의 처음부터 시작한다.
        right = len(lis) # LIS의 길이까지 검사한다.

        while left < right: # 이분 탐색을 수행한다.
            mid = (right + left) // 2 # 중간값을 찾는다.
            if lis[mid] < case: # 중간값이 case보다 작은 경우,
                left = mid + 1 # 왼쪽 영역을 제외한 오른쪽 영역에서 검색한다.
            else: # 중간값이 case보다 크거나 같은 경우,
                right = mid # 오른쪽 영역을 제외한 왼쪽 영역에서 검색한다.
        lis[right] = case # LIS의 마지막 값보다 작은 값을 발견한 경우, 그 위치에 값을 저장한다.

print(lis) # LIS 리스트를 출력한다.
