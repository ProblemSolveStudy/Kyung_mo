def solution(board):
    answer = -1
    
    cnt_o, cnt_x, win_o, win_x = 0, 0 , 0, 0
    
    for b in board:
        cnt_o += b.count('O')
        cnt_x += b.count('X')
    
    if cnt_o + cnt_x == 0:
        return 1
    if cnt_o > cnt_x + 1:
        return 0
    if cnt_o < cnt_x:
        return 0
    
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[1][i] == 'O':
                win_o += 1
            elif board[1][i] == 'X':
                win_x += 1
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][1] == 'O':
                win_o += 1
            elif board[i][1] == 'X':
                win_x += 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[1][1] == 'O':
            win_o += 1
        elif board[1][1] == "X":
            win_x += 1
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[1][1] == 'O':
            win_o += 1
        elif board[1][1] == 'X':
            win_x += 1
    
    if win_x == win_o and win_o == 0:
        return 1
    if win_x == 0 and win_o > 0:
        if cnt_x < cnt_o:
            return 1
    if win_x > 0 and win_o == 0:
        if cnt_x == cnt_o:
            return 1
    return 0

print(solution(["OOO", "...", "XXX"]))