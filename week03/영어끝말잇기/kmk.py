def solution(n, words):
  previous = set()   #이전에 말한 단어들
    
  turn = [0 for _ in range(n+1)]  #person마다 턴 수
  person = 1 
    
  for i in range(len(words)):
    turn[person] += 1
    if words[i] in previous: #이미 전에 말한 단어라면
      return [person, turn[person])
    elif words[i-1][-1] != words[i][0] and i != 0:  #끝말이 이어지지 않는다면
      return [person, turn[person])
    else:
      previous.add(words[i])
      if person >= n:
        person = 1
      else:
        person += 1
              
  return [0,0]
