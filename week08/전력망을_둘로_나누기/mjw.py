# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import defaultdict

def dfs(cur, graph, visited):
    visited[cur] = 1
    for node in graph[cur]:
        if not visited[node]:
            visited = dfs(node, graph, visited)
    return visited

def solution(n, wires):
    graph = defaultdict(set)
    for a, b in wires:
        graph[a].add(b)
        graph[b].add(a)
    
    min_abs = 1e9
    for a, b in wires:
        graph[a] -= {b}
        graph[b] -= {a}
        
        n1 = dfs(a, graph, visited=[0]*(n+1))
        n2 = dfs(b, graph, visited=[0]*(n+1))
        min_abs = min(abs(sum(n1)-sum(n2)), min_abs) if n1!=n2 else min_abs
        
        graph[a] |= {b}
        graph[b] |= {a}
    return min_abs
