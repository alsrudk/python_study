# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):     #     1  2  3
    users = [0]*(n+1)       # [0, 0, 0, 0]
    
    visited = set()
    last_c = words[0][0]

    turn = 1
    for word in words:
        users[turn] += 1    # [0, 1, 0, 0]
        
        if last_c != word[0] or word in visited:
            return [turn, users[turn]]
        
        visited.add(word)
        turn = turn + 1 if turn < n else 1
        last_c = word[-1]
        
    return [0,0]
