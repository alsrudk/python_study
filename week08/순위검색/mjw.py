from collections import defaultdict
from itertools import product

def binary_search(target, arr):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] >= target:
            end = mid - 1
            
    if arr[start] < target:
        return start + 1
    return start
            
def solution(info, query):
    INFO = defaultdict(list)
    for info_ in info:
        lang, job, career, food, score = info_.split()
        score = int(score)
        for x in product(*[('-',lang), ('-',job), ('-',career), ('-',food)]):
            INFO[x].append(score)
            
    for v in INFO.values():
        v.sort()
    
    answer = []
    for q in query:
        lang, job, career, food_score = q.split(' and ')
        food, score = food_score.split()
        score = int(score)
        
        users = INFO[(lang, job, career, food)]
        if not users:
            answer.append(0)
        else:
            idx = binary_search(score, users)
            answer.append(len(users)-idx)

    return answer
