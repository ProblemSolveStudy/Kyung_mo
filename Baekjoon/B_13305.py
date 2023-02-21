# 우선 맨 처음엔 무조건 주유를 해야한다.
# 다음 도시의 주유비가 지금 도시보다 싸다면 다음 도시 도로만큼만 넣는다
# 다음 도시의 주유비가 지금 도시보다 비싸다면 현재 도시에서 다다음 도로까지 넣는것과 다음도시에서 한번 더 주유하는 것을 비교한다.


# import sys

# input = sys.stdin.readline
# cost = 0
# # 도시의 개수
# n = int(input())

# way = list(map(int, input().rstrip().split()))
# city = list(map(int, input().rstrip().split()))

# cost = city[0] * way[0]

# cheapest = city[0]

# for i in range(1, n-1):
#     if city[i] <= cheapest:
#         cheapest = city[i]
#         cost += cheapest * way[i]
#     else:
#         cost += cheapest * way[i]

# print(cost)

import sys
input = sys.stdin.readline

n = int(input())

way = list(map(int, input().rstrip().split()))
city = list(map(int, input().rstrip().split()))

cost = way[0] * city[0]

cheapestCity = city[0]
for i in range(1, len(city)-1):
    if city[i] <= cheapestCity:
        cheapestCity = city[i]
        cost+=cheapestCity * way[i]
    else:
        cost += cheapestCity * way[i]

print(cost)