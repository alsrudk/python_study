from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    start, dest = (0,0), (n-1, m-1)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # bfs
    queue = deque([(start, 1)]) # [(위치, 이동거리), ]
    visited = set()

    while queue:
        (r,c), depth = queue.popleft()
        nexts = [(r+dx,c+dy) for (dx,dy) in moves if (0<=r+dx<n) and (0<=c+dy<m) and (maps[r+dx][c+dy] == 1)]
        depth += 1
        for nxt in nexts:
            if nxt not in visited:
                if nxt == dest:
                    return depth
                queue.append((nxt, depth))
        visited |= set(nexts)
    return -1
