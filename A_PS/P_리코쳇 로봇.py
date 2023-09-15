from collections import deque
def solution(board):
    answer = 0
    r,c = len(board), len(board[0])
    visited = [[0] * c for _ in range(r)]

    dx, dy = [-1, 1, 0 ,0], [0, 0, -1, 1]
    def bfs(x,y):
        q = deque([(x,y)])
        visited[x][y] = 1
        while q:
            x,y = q.popleft()
            if board[x][y] == 'G':
                return visited[x][y]
            for i in range(4):
                nx,ny = x, y
                while True:
                    nx,ny = nx + dx[i], ny + dy[i]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx<0 or nx>=r or ny<0 or ny>=c:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
        return -1

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                answer = bfs(i,j)

    if answer > 0:
        answer -= 1

    return answer

board = [".D.R", "....", ".G..", "...D"]
print(solution(board))