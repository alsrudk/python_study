# https://school.programmers.co.kr/learn/courses/30/lessons/42884#

def solution(routes):
    routes.sort(key=lambda x: x[0])
    
    answer = 0
    prev = routes[0]    # 이전 카메라가 설치된 구간
    i = 1
    while i < len(routes):
        cur = routes[i]
        if prev[1] < cur[0]:
            answer += 1
            prev = cur
        else:
            prev = [max(prev[0], cur[0]), min(prev[1], cur[1])]
        i += 1
    return answer+1
