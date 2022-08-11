# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    k = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            k += 1
    return k
