# https://school.programmers.co.kr/learn/courses/30/lessons/42884#

def solution(routes):
    routes.sort(key=lambda x: (x[0], -x[1])) # 진입 지점이 빠른 순 > 주행 거리 긴 순
    
    answer = 0
    prev = routes[0]
    i = 1
    while i < len(routes):
        cur = routes[i]
        if prev[1] < cur[0]:
            answer += 1
            prev = routes[i]
        else:
            prev = [max(prev[0], cur[0]), min(prev[1], cur[1])]
        i += 1
    return answer+1
