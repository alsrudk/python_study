# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    n_rows, n_cols = len(board), len(board[0])

    maxi = 1 if max(board[0])==1 or max([board[i][0] for i in range(n_rows)])==1 else 0
    
    for i in range(1, n_rows):
        for j in range(1, n_cols):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                maxi = max(maxi, board[i][j])
    
    return maxi**2

# [0, 1, 1, 1]
# [1, 1, 2, 2]
# [1, 2, 2, 3]
# [0, 0, 1, 0]
