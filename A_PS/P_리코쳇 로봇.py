from collections import deque
def solution(board):
    answer = 0
    
    c,r = len(board), len(board[0])
    visited = [[0] * r for _ in range(c)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(i,j):
        q = deque([(i,j)])
        visited[i][j] = 1
        while q:
            x,y = q.popleft()
            if board[x][y] == 'G':
                return visited[x][y]
            for i in range(4):
                nx, ny = x, y
                while True:
                    nx, ny = nx+dx[i], ny+dy[i]
                    if 0<=nx<c and 0<=ny<r and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx<0 or nx>=c or ny<0 or ny>=r:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
        return -1
    
    for i in range(c):
        for j in range(r):
            if board[i][j] == 'R':
                answer = bfs(i,j)
    
    if answer > 0:
        answer -=1
    return answer

board = [".D.R", "....", ".G..", "...D"]
print(solution(board))