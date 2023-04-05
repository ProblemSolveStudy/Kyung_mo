# mid값이 개똥벌레의 나는 위치
# total값이 부서진 장애물의 수
# 석순 한번, 종유석 한번 이렇게 진행해야 하나?
# 
import sys

n,h = map(int, sys.stdin.readline().split())

lines = [0] * h

for i in range(n):
    high = int(sys.stdin.readline().rstrip())

    if i%2 == 0: # 종유석
        lines[h-high] += 1
    else:
        lines[high] += 1


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
            


# start = 0
# end = h
# result = 0
# min_total = n

# while start <= end:
#     mid = (start + end) // 2
#     total = 0

#     for x in odd:
#         if mid <= x:
#             total += 1

#     for y in even:
#         if mid > h-y:
#             total += 1
    
#     if total < min_total:
#         min_total = total
#         result = mid
#         start = mid + 1
#     else:
#         end = mid - 1

# print(min_total, mid)