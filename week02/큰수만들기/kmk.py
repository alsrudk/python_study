def solution(number, k):
    answer = []
    
    for idx, num in enumerate(number):
        #answer안에 원소 존재, 새로 들어올 수가 answer의 마지막 수보다 크고, k>0
        while answer and answer[-1] < num and k>0: 
            answer.pop()
            k -= 1
        #k=0 되면 나머지 숫자들 그대로 붙여줌
        if k == 0:     
            answer += number[idx:]
            break
        answer.append(num)

    #k가 0이 되지 않았을 경우를 처리해줌
    return ''.join(answer[:len(answer)-k])

  
  

'''
4177252841  k=4
4
4 1 
4             -1 
7             -1
7 7
7 7 2
7 7 5         -1
7 7 5 2 
7 7 5 8       -1   <- k=0
7 7 5 8 4 1   answer += number[idx:]
-----------------------------------------
54321        k=2
5 
5 4
5 4 3
5 4 3 2 1    그대로 k=2

answer[:len(answer)-k]

'''
