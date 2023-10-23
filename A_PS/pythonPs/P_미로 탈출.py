from collections import deque
def solution(maps):
    answer = 0
    start, lever = find_points(maps)
    lever_dist = bfs(lever, maps, 'L')
    end_dist = bfs(start,maps,'E')
    
    print(lever_dist, end_dist)
    return answer

def find_points(maps):
    c,r = len(maps), len(maps[0])
    for i in range(c):
        for j in range(r):
            if maps[i][j] == 'S':
                start = (i,j)
            elif maps[i][j] == 'L':
                lever = (i,j)
    return start, lever

def bfs(start, maps, target):
    dx,dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    c,r = len(maps), len(maps[0])
    visited = [[False] * r for _ in range(c)]
    x,y = start
    q = deque([(x,y,0)])
    visited[x][y] = True
    
    while q:
        x,y, dist = q.popleft()
        if maps[x][y] == target:
            return dist
        
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<c and 0<=ny<r and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx,ny,dist+1))
    return -1

