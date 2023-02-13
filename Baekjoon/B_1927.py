# 1. 배열에 자연수 x를 넣는다
# 2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# * 만약 x가 자연수라면 x>0이라면 배열에 x라는 값을 넣고 만약 x==0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거한다.

import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, x)
    elif x==0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))