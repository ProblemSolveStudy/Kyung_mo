from collections import deque
def solution(maps):
    r,c = len(maps), len(maps[0])
    result = []
    visited = [[False] * c for _ in range(r)]
    dx,dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def bfs(x,y):
        q = deque([(x,y)])
        visited[x][y] = True
        cnt = int(maps[x][y])
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<r and 0<=ny<c and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += int(maps[nx][ny])
                    q.append((nx,ny))
        return cnt
                    
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and not visited[i][j]:
                result.append(bfs(i,j))
    
    if len(result) > 0:
        result.sort()
    else:
        result.append(-1)
    return result

solution(["XXX","XXX","XXX"])