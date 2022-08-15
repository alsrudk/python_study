# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    cnt = 1
    matches = [(i,i+1) for i in range(1, n, 2)]  # [(1, 2), (3, 4), (5, 6), (7, 8)]
    
    a, b = sorted([a, b])
    while (a,b) not in matches:
        cnt += 1
        tmp = []
        for match in matches:
            if a in match:
                tmp.append(a)
            elif b in match:
                tmp.append(b)
            else:
                tmp.append(match[0])                                  # [1, 4, 5, 7]
        matches = [(tmp[i],tmp[i+1]) for i in range(0, len(tmp), 2)]  # [(1, 4), (5, 7)]
    return cnt
