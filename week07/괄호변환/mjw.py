# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def is_correct(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if not stack or stack[-1] == ')':
                return False
            stack.pop()
    return True if not stack else False

def trans(s):
    return s.replace('(','_').replace(')','(').replace('_',')')

def split_uv(w):
    for i in range(2, len(w)):
        u, v = w[:i], w[i:]
        if u.count('(') == u.count(')'): # balance_string
            return u, v
    return w, ''

def solution(w):
    if w == '':
        return w
    u, v = split_uv(w)
    if is_correct(u):
        return u + solution(v)
    return '(' + solution(v) + ')' + trans(u[1:-1])
