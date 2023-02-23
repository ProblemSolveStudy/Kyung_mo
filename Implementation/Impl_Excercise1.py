import sys

# 이건 내풀이

# N = int(sys.stdin.readline())

# arr = list(sys.stdin.readline().rstrip().split())

# start = [1,1]

# for i in arr:
#     if i == 'R':
#         if start[1] + 1 > 100:
#             continue
#         start[1] += 1
#     elif i == 'L':
#         if start[1] - 1 < 1:
#             continue
#         start[1] -= 1
#     elif i == 'U':
#         if start[0] - 1 < 1:
#             continue
#         start[0] -= 1
#     elif i =='D':
#         if start[0] + 1 > 100:
#             continue
#         start[0] += 1

# print(*start)

# 동빈나's 풀이

n = int(sys.stdin.readline())
x, y = 1, 1
arr = list(sys.stdin.readline().rstrip().split())

# L, R, U, D 이동방향
move_types = ['L', 'R', 'U', 'D']   
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in arr:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    
    if nx<1 or ny < 1 or nx> n or ny>n:
        continue

    x, y= nx, ny
print(x, y)