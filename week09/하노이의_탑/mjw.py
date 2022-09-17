# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def hanoi(n, from_, by_, to_, res):
    if n == 1:
        return res + [[from_, to_]]
    # 2로 (n-1)개 이동, 맨 밑 1->3, 3로 (n-1)개 이동
    return hanoi(n-1, from_, to_, by_, res) + [[from_, to_]] + hanoi(n-1, by_, from_, to_, res)

def solution(n):
    return hanoi(n, 1, 2, 3, [])
