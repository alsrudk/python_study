def solution(citations):
    answer = 0
    
    for i,h in enumerate(sorted(citations, reverse=True)):
        if i >= h:
            answer += i
            break
    else:
        answer += len(citations)
    return answer
