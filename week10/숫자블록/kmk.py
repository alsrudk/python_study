import math
def solution(begin, end):
    num = list(range(begin, end+1))
    answer = [1] * (end-begin+1)
    if begin == 1:
        answer[0] = 0
        
    for i in range(len(num)):
        for n in range(2, int(math.sqrt(num[i]))+1):
            if num[i]%n == 0 and num[i]//n <= 10000000:
                answer[i] = num[i]//n
                break
    
    return answer
