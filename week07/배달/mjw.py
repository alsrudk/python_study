# https://school.programmers.co.kr/learn/courses/30/lessons/12978

from collections import defaultdict
from heapq import heappush, heappop

def solution(N, road, K):
    graph = defaultdict(lambda:defaultdict(lambda:1e9))
    for a, b, c in road:
        graph[a][b] = min(c, graph[b][a])
        graph[b][a] = graph[a][b]
        
    start = 1
    distance = {k:1e9 for k in range(1,N+1)}
    distance[start] = 0
    
    # dijkstra
    queue = []
    heappush(queue, [0, start])
    while queue:
        cost, cur = heappop(queue)
        if distance[cur] < cost:
            continue
        for nxt, nxt_cost in graph[cur].items():
            nxt_cost += cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heappush(queue, [nxt_cost, nxt])
    
    return sum([1 for v in distance.values() if v <= K])
