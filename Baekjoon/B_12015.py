# import sys
# from bisect import bisect_left, bisect_right
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0]

# for a in arr:
#     if dp[-1] < a:
#         dp.append(a)
#     else:
#         dp[bisect_left(dp,a)] = a

# print(len(dp) - 1)


import sys
input = sys.stdin.readline

n = int(input())
cases = list(map(int, input().split()))
lis = [0]

for case in cases:
    if lis[-1]<case:
        lis.append(case)
    else:
        left = 0
        right = len(lis)

        while left<right:
            mid = (right+left)//2
            if lis[mid]<case:
                left = mid+1
            else:
                right = mid
        lis[right] = case

print(lis)