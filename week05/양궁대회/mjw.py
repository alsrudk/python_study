# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def score_gap(ryan, appeach):
    r_score, a_score = 0, 0
    for k in ryan.keys():
        if ryan[k] > appeach[k]:
            r_score += k
        elif appeach[k] > 0:
            a_score += k
    return r_score - a_score

def search(score, n, appeach, ryan, max_gap=0, answer={}):
    if sum(ryan.values()) == n:
        return ryan

    for s in range(score,-1,-1):
        need_n = appeach[s]+1 if s>0 else n-sum(ryan.values())
        if sum(ryan.values()) + need_n > n: 
            continue
        ryan_ = ryan.copy()
        ryan_[s] = need_n
        ryan_ = search(s-1, n, appeach, ryan_, max_gap, answer)

        cur_gap = score_gap(ryan_, appeach)
        if cur_gap > max_gap:
            answer = ryan_.copy()
            max_gap = cur_gap
        elif cur_gap == max_gap:
            if sum([k for k, v in ryan_.items() if v > 0]) > sum([k for k, v in answer.items() if v > 0]):
                answer = ryan_.copy()
    
    if max_gap == 0 or not answer:
        return {}
    
    return answer

def solution(n, info):
    appeach = {10-i:k for i, k in enumerate(info)}
    ryan = {10-i:0 for i, k in enumerate(info)}
    
    answer = search(10, n, appeach, ryan)
    if not answer:
        return [-1] 
    return list(answer.values())
