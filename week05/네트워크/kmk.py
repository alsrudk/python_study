def dfs(i, visited, graph):
    visited[i] = True   
    for i in graph[i]:   
        if visited[i] == False:
            dfs(i, visited, graph)
    
def solution(n, computers):
    answer = 0
    visited = [False]*n             
    graph = [[] for _ in range(n)]   
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    for i in range(n):
        if visited[i] == False:
            answer += 1
            dfs(i, visited, graph)
    
    return answer
