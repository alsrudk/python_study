# https://school.programmers.co.kr/learn/courses/30/lessons/12913

from copy import deepcopy

def solution(land):
    dp = deepcopy(land)
    for r in range(1, len(land)):
        for i in range(4):
            dp[r][i] = land[r][i] + max(dp[r-1][:i]+dp[r-1][i+1:])
    return max(dp[-1])
