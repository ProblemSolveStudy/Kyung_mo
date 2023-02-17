import sys
import heapq

n = int(sys.stdin.readline())

roomList = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

roomList.sort()

roomQueue = []
heapq.heappush(roomQueue, roomList[0][1]) # 끝나는 시간 확인하기

for i in range(1, n):
    if roomList[i][0] < roomQueue[0]:
        heapq.heappush(roomQueue, roomList[i][1])
    else:
        heapq.heappop(roomQueue)
        heapq.heappush(roomQueue, roomList[i][1])

print(len(roomQueue))