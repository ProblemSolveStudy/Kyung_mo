import sys, heapq
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    heapq.heappush(lst, int(sys.stdin.readline()))
result = 0
if len(lst) == 1:
    print(0)
else:
    while len(lst) > 1:
        num1 = heapq.heappop(lst)
        num2 = heapq.heappop(lst)

        result += num1+num2
        heapq.heappush(lst, num1+num2)
    print(result)