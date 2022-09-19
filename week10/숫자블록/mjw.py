# https://school.programmers.co.kr/learn/courses/30/lessons/12923

def get_divisor(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and n//i <= 1e7:
            return n//i
    return 1

def solution(begin, end):
    answer = []
    for n in range(begin, end+1):
        if n == 1:
            answer.append(0)
        else:
            answer.append(get_divisor(n))
    return answer
