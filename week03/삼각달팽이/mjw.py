# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    tri_list = [[0]*i for i in range(1,n+1)]  # [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]
    dest_num = len(sum(tri_list, []))
    
    num = 1
    r,c = 0,0                                 # 현재 위치
    
    move, m_idx = [(1,0),(0,1),(-1,-1)], 0    # [↓, →, ↑] , 현재 이동 방향
    lap = 0                                   # 채운 바퀴 수

    while num <= dest_num:
        tri_list[r][c] = num
        num += 1
        
        if r+move[m_idx][0] == n-lap:
            m_idx = 1
        
        elif c+move[m_idx][1] == len(tri_list[r])-lap:
            m_idx = 2

        elif tri_list[r+move[m_idx][0]][c+move[m_idx][1]] != 0:
            m_idx = 0
            lap += 1
            
        r += move[m_idx][0]
        c += move[m_idx][1]
    
    return sum(tri_list, [])
