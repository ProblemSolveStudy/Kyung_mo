import sys, heapq

n = int(sys.stdin.readline())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = []

rooms.sort()
heapq.heappush(answer, rooms[0][1])

for i in range(1, n):
    if answer[0] > rooms[i][0]:
        heapq.heappush(answer, rooms[i][1])
    else:
        heapq.heappop(answer)
        heapq.heappush(answer, rooms[i][1])

print(len(answer))