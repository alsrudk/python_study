def solution(msg):
  answer = []
  
  index = {}
  for i in range(26):
    index[chr(65+i)] = i+1
    
  cur, next = 0, 0
  while True:
    next += 1
    if next == len(msg):
      answer.append(index[msg[cur:next]])
      break
    if msg[cur:next+1] not in index:
      index[msg[cur:next+1]] = len(index) + 1
      answer.append(index[msg[cur:next]])
      cur = next
      
  return answer
    
