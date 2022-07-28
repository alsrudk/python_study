# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for x in s:
        if not stack or x == '(':
            stack.append(x)
        if stack[-1] == '(' and x == ')':
            stack.pop()
    if stack:
        return False
    return True
