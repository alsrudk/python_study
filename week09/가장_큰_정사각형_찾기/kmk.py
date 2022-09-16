def solution(board):
    answer = []
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            if board[r][c] == 1:
                board[r][c] = min(board[r-1][c-1], board[r-1][c], board[r][c-1])+1
    for row in board:
        answer.append(max(row))
        
    return max(answer)**2
    
