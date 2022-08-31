import heapq
def dijkstra(start, graph, distance, gates, summits):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = max(dist, i[1])
            if i[0] not in gates and cost < distance[i[0]]:
                distance[i[0]] = cost
                if i[0] not in summits:
                    heapq.heappush(queue, (cost, i[0]))
    return distance

def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    for path in paths:
        i,j,w = path
        graph[i].append((j,w))
        graph[j].append((i,w))
    distance = [int(1e9)] * (n+1)
    for summit in summits:
        graph[summit] = ()
    
    for gate in gates:
        dijkstra(gate, graph, distance, gates, summits)
    summits.sort(key=lambda x:(distance[x], x))
    return [summits[0], distance[summits[0]]]
    
