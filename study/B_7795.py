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

# a가 b보다 큰 쌍의 개수 찾기

import sys
input = sys.stdin.readline

def binary_search(target):
    start = 0
    end = len(b)-1
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        if b[mid] < target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


for _ in range(int(input())):
    _,_ = map(int, input().split()) # 사용하지 않는 (N,B)
    a = sorted(list(map(int, input().split()))) # 정렬하면서 값 받아오기
    b = sorted(list(map(int, input().split()))) # 정렬하면서 값 받아오기
    total = 0 # pair의 개수 총합
    for x in a: # a가 b보다 큰 쌍의 개수 찾기 이므로 target은 a의 값 x
        if x > b[0]: # x의 값이 b[0] (정렬되어있으므로, 가장 작은 값) 보다 작다면 굳이 이분탐색을 할 필요가 없음
            total += binary_search(x) + 1 # 이분탐색 시작 (이분탐색 시 return값은 index값 그러므로 +1을 해줘야 target이 들어갈 index값의 결과가 나옴 )
    print(total)