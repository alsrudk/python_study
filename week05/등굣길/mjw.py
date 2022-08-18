# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    arr = [[1]+[0]*(n-1) if i > 0 else [1]*n for i in range(m)]
    
    is_puddle = [[0]*n for _ in range(m)]
    for (i,j) in puddles:
        i, j = i-1, j-1
        is_puddle[i][j] = 1
        arr[i][j] = 0
        
        if i == 0:
            arr[0][j:] = [0]*len(arr[0][j:])
        if j == 0:
            for k in range(i, m):
                arr[k][0] = 0
    
    for i in range(1,m):
        for j in range(1,n):
            if is_puddle[i][j] == 1:
                continue
            arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000007
            
    return arr[m-1][n-1]
