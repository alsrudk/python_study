def dfs(n,graph):
    stack = [n]
    visited = [n]
    while stack:
        v = stack.pop()
        for node in graph[v]:
            if node not in visited:
                visited.append(node)
                stack.append(node)
    return len(visited)

def solution(n, wires):
    answer = int(1e9)
    for i in range(len(wires)):            
        wires_ = wires[:i]+wires[i+1:]     
        graph = [[] for _ in range(n+1)]   
        for wire in wires_:
            v1, v2 = wire
            graph[v1].append(v2)
            graph[v2].append(v1)
        result = abs(dfs(wires[i][0],graph)-dfs(wires[i][1],graph))
        answer = min(answer, result)
    return answer
        
   
