def solution(land):
    answer = 0
    r, c = len(land), len(land[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    
    for j in range(c):
        dp[0][j] = land[0][j]

    for i in range(1, r):
        for j in range(c):
            score = 0
            for idx in range(c):
                if idx == j:
                    continue
                if score < dp[i-1][idx]:
                    score = dp[i-1][idx]
            dp[i][j] = land[i][j]+score
    return max(dp[r-1])
