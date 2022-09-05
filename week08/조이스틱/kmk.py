def dfs(cur_move, cur_idx, answer, name):
    answer += cur_move[cur_idx]
    cur_move[cur_idx] = 0
    
    if sum(cur_move) == 0:
        return answer
    
    right_move, left_move = 1,1
    
    left_idx = 0
    while True:
        if cur_idx-left_move < 0:
            left_idx = cur_idx-left_move+len(name)
        else:
            left_idx = cur_idx-left_move
        if cur_move[left_idx] != 0:
            break
        left_move += 1
    cur_move_left = cur_move.copy()
    
    right_idx = 0
    while True:
        if cur_idx+right_move > len(name)-1:
            right_idx = cur_idx+right_move-len(name)
        else:
            right_idx = cur_idx+right_move
        if cur_move[right_idx] != 0:
            break
        right_move += 1
    cur_move_right = cur_move.copy()
    
    result_left = dfs(cur_move_left, left_idx, answer+left_move, name)
    result_right = dfs(cur_move_right, right_idx, answer+right_move, name)
    return min(result_left, result_right)

def solution(name):
    answer = 0
    move = [0] * len(name)
    for i in range(len(name)):
        move[i] = min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
       
    return dfs(move, 0, 0, name)
