# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    move = {'U':(0,1), 'L':(-1,0), 'R':(1,0), 'D':(0, -1)}
    visited = set()
    
    cur = (0,0)
    for d in dirs:
        mv = move[d]
        nxt = (cur[0]+mv[0], cur[1]+mv[1])
        if (-5<=nxt[0]<=5) and (-5<=nxt[1]<=5):
            visited.add(tuple(sorted((cur,nxt)))) # ((1,0),(0,0)) -> ((0,0),(1,0))
            cur = nxt
            
    return len(visited)
