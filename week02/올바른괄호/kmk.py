def solution(s):
    answer = []
    for p in s:
        if p == '(':
            answer.append(p)
        elif p == ')':
            if answer:
                answer.pop()  #맞는 짝이 있음 
            else:
                return False  #맞는 짝이 없음
    
    if answer:                #남아있다는건 짝이 없다는 것
        return False
    else:
        return True
