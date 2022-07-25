# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)                # [3, 0, 6, 1, 5] -> [6, 5, 3, 1, 0]
    for h in range(len(citations), 0, -1):      
        if citations[h-1] >= h:                 # (h-1)번째 논문이 h번 이상 인용되었다면 -> H-Index
            return h
    return 0
