# https://school.programmers.co.kr/learn/courses/30/lessons/17679

from copy import deepcopy
import numpy as np

def remove(m, n, board):
    rm_num = 0
    board_ = deepcopy(board)
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == '': continue
            elif board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                for x,y in [(i,j), (i+1,j), (i,j+1), (i+1,j+1)]:
                    if board_[x][y] != '': rm_num += 1
                    board_[x][y] = ''
    return board_, rm_num

def relocate(m, n, board):
    board = np.array(board).T.tolist()
    for i in range(n):
        tmp = ''.join(board[i])
        board[i] = ['']*(m-len(tmp)) + list(tmp)
    return np.array(board).T.tolist()

def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    ans = 0
    while True:
        board, rm_num = remove(m, n, board)
        if rm_num == 0: break
        else:
            ans += rm_num
        board = relocate(m, n, board)
    return ans
