import heapq
def dijkstra(start, graph, distance):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

def solution(N, road, K):
    answer = 0  
    graph = [[] for _ in range(N+1)]
    distance = [int(1e9)] * (N+1)
    
    for r in road:
        a,b,c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    dijkstra(1, graph, distance)
    for d in distance:
        if d <= K:
            answer += 1

    return answer
