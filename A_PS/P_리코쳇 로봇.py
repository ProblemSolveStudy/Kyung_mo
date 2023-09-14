from collections import deque
def solution(board):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0] * len(board[0]) for _ in range(len(board))]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        visited = [[0] * len(board[0] for _ in range(len(board)))]
        visited[x][y] = 1

        while q:
            x,y = q.popleft()
            if board[x][y] == 'G':
                return visited[x][y]
            for i in range(4):
                while True:
                    nx, ny = nx+dx[i] , 
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                answer = bfs(i,j)
    return answer

print(solution(board=["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))