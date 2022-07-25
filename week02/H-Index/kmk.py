def solution(citations):
    answer = 0
    citations.sort(reverse = True)        #내림차순 정렬
    n = len(citations)                    #전체 논문 개수
                   
    for num in range(n, -1, -1): 
        count = 0                         #num번 이상 인용된 논문 개수 count
        for citation in citations:
            if citation >= num:  
                count += 1
        if count >= num:                  #처음으로 만족하는게 h-index 최대값
            answer = num
            break
    
    return answer
