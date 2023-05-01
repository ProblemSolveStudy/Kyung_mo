# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(2)]

#     if n == 1:
#         print(max(arr[0][0], arr[1][0]))
#     else:
#         arr[0][1] += arr[1][0]
#         arr[1][1] += arr[0][0]
#         for i in range(2, n):
#             arr[0][i] += max(arr[1][i-1], arr[1][i-2])
#             arr[1][i] += max(arr[0][i-2], arr[0][i-1])
        
#         print(max(arr[0][n-1], arr[1][n-1]))


# 재풀이
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    if n == 1:
        print(max(map(max,arr)))
        
    else:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        

        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[1][1] + arr[0][0]


        for i in range(2, n):
            dp[0][i] = max(arr[0][i] + dp[1][i-1], dp[1][i-2] + arr[0][i])
            dp[1][i] = max(arr[1][i] + dp[0][i-1], dp[0][i-2] + arr[1][i])
        print(max(map(max, dp)))