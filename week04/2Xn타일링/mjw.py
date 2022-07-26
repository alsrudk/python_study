# https://school.programmers.co.kr/learn/courses/30/lessons/12900#

from collections import defaultdict

def solution(n):
    dp = defaultdict(int)
    for i in range(1, n+1):
        if i < 3:
            dp[i] = i
        else:
            dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    return dp[n]
