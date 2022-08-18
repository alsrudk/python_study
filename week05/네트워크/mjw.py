from collections import defaultdict

def dfs(cur, graph, visited):
    new_nodes = (graph[cur] - visited)
    if not new_nodes:
        return visited
    
    for nxt in new_nodes:
        visited.add(nxt)
        visited = dfs(nxt, graph, visited)
    return visited
    
def solution(n, computers):
    computer_ids = set(range(n))    # computer_ids = {0, 1, 2}
    graph = defaultdict(set)        # graph = {0: {0, 1}, 1: {0, 1}, 2: {2}})
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].add(j)
    
    cnt = 0
    visited = set()
    while len(visited) < n:
        cur = (computer_ids - visited).pop()
        visited.add(cur)
        visited = dfs(cur, graph, visited)
        cnt += 1
    return cnt
