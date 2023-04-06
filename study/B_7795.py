# A가 B를 먹는다.
# A는 자기보다 작은 먹이만 먹을 수 있음
# A와 B가 주어졌을 때 A가 씹어먹을 수 있는 쌍이 몇개가 있는지 구하라


# 걍 3중포문도 가능하긴 함
# for k in range(T):
#     for i in range(len(a_arr)):
#         for j in range(len(b_arr)):
#             if a_arr[i]>b_arr[j]:
#                 cnt += 1
#     print(cnt)
# 근데 분명히 시간초과가 날것임
# 20000 ^ 3 = 80억 (80초)
# 즉 O(log n)의 시간복잡도를 가져야만 한다.

def binary_search(target):
    start = 0
    end = len(b)-1
    total = 0
    while start <= end:
        mid = (start + end) // 2
        if b[mid] < target:
            start = mid + 1
            total = mid
        else:
            end = mid - 1
    return total + 1

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    _,_ = map(int, input().split())
    # 1 1 3 7 8
    a = sorted(list(map(int, input().split())))
    # 1 3 6
    b = sorted(list(map(int, input().split())))
    result = 0
    for x in a:
        if b[0] < x:
            t = binary_search(x)
            result += t
    print(result)