import sys, heapq
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n): # O(n)
    heapq.heappush(heap, int(input())) # O(logn)
result = 0
if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1: # O(n)
        num1 = heapq.heappop(heap) # O(logn)
        num2 = heapq.heappop(heap)
        result += num1 + num2
        heapq.heappush(heap, num1+num2) # O(logn)
    print(result)