# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def convert(num, n_base):
    T = "0123456789ABCDEF"
    q, r = divmod(num, n_base)
    if q == 0:
        return T[r]
    else:
        return convert(q, n_base) + T[r]

def n_generator(k, n_base):
    i = 0
    num = 0
    converted_num = convert(num, n_base)
    c_idx = 0
    while i <= k:
        yield converted_num[c_idx]
        if c_idx < len(converted_num)-1:
            c_idx += 1
        else:
            num += 1
            converted_num = convert(num, n_base)
            c_idx = 0
        i += 1
    
def solution(n, t, m, p):
    ans = ''
    for turn_idx, x in enumerate(n_generator(t*m, n), 1):
        turn_idx %= m
        if turn_idx == p or (turn_idx==0 and m==p):
            ans += x
        if len(ans) == t:
            return ans
    return ans
