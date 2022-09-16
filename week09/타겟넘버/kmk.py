def dfs(idx, numbers, target, cur, result = [], answer = 0):
    if idx == len(numbers):
        if sum(cur) == target:
            result.append(cur)
        return
    dfs(idx+1, numbers, target, cur+[numbers[idx]])
    dfs(idx+1, numbers, target, cur+[-numbers[idx]])
    return len(result)
    
    
def solution(numbers, target):
    return dfs(0, numbers, target, [])    
