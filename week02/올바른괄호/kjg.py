def solution(s):
    answer = True
    #개수가 같아야함
    #순서가 맞아야함
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        answer = False
    
    return answer
