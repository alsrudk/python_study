# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def search(names, visited, cursor, cnt, min_cnt=1e9):
    if cnt >= min_cnt:
        return min_cnt
    
    cnt += names[cursor]
    visited[cursor] = 1
    
    if sum(visited) == len(names):
        return cnt

    # search right
    cur, move = cursor, 0
    while visited[cur]==1:
        cur = cur+1 if cur < len(names)-1 else 0
        move += 1
    min_cnt = min(search(names, visited.copy(), cur, cnt+move, min_cnt), min_cnt)
        
    # search left
    cur, move = cursor, 0
    while visited[cur]==1:
        cur = cur-1 if cur > 0 else len(names)-1
        move += 1
    min_cnt = min(search(names, visited.copy(), cur, cnt+move, min_cnt), min_cnt)
    return min_cnt
    
def get_changeCnt(x):
    ordx = ord(x)-65
    return min(ordx, 26-ordx)

def solution(name):
    if set(name) == {'A'}:
        return 0
    names = list(map(lambda x:get_changeCnt(x), name))
    visited = [0 if x > 0 else 1 for x in names]
    return search(names, visited, cursor=0, cnt=0, min_cnt=1e9)
