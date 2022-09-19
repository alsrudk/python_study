def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    
    while routes:
        location = routes[0][1]
        visit = []
        for i in range(len(routes)):
            if routes[i][0] <= location:
                visit.append(routes[i])
        for car in visit:
            routes.remove(car) 
        answer += 1
        
    return answer
