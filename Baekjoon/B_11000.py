# import sys

# n = int(sys.stdin.readline())
# rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# rooms.sort(key=lambda x: (x[0], x[1]))

# room=[]
# for start, end in rooms:
#     if not room:
#         room.append(end)
#     else:
#         allocated = False
#         for i in range(len(room)):
#             if room[i] <= start:
#                 room[i] = end
#                 allocated = True
#                 break
        
#         if not allocated:
#             room.append(end)

# print(len(room))

import heapq, sys
input = sys.stdin.readline
n = int(input())

q = []
for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))