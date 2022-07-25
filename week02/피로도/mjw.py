# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 피로도

def dfs(cur_k, dungeons, n_dungeon=0):
    if not dungeons or cur_k < dungeons[-1][0]:
        return n_dungeon
    
    max_n_dungeon = 0
    for i, d in enumerate(dungeons):
        if cur_k >= d[0]:
            max_n_dungeon = max(max_n_dungeon, dfs(cur_k-d[1], dungeons[:i]+dungeons[i+1:], n_dungeon+1))
    return max_n_dungeon

def solution(k, dungeons):
    dungeons.sort(key=lambda x: x[0], reverse=True)
    return dfs(k, dungeons)
