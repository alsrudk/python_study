def solution(n, words):
    answer = []
    previous = set()   #이전에 말한 단어들
    
    turn = [0 for _ in range(n+1)]  #person마다 턴 수
    person = 1 
    
    for i in range(len(words)):
        if words[i] in previous:  #이미 전에 말한 단어라면
            turn[person] += 1
            answer.append(person)
            answer.append(turn[person])
            return answer
        elif words[i-1][-1] != words[i][0] and i != 0:  #끝말이 이어지지 않는다면
            turn[person] += 1
            answer.append(person)
            answer.append(turn[person])
            return answer
        else:
            previous.add(words[i]) 
            turn[person] += 1
            if person >= n:
                person = 1
            else:
                person += 1
    return [0,0]
