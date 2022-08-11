def solution(msg):
  answer = []
  
  index = {}
  for i in range(26):
    index[chr(65+i)] = i+1
  msg = list(msg)
  
  while True:
    for j in range(1, len(msg)+1):
      key = ''.join(msg[:j])
      if key in index:
        if j == len(msg):
          answer.append(index[key])
          return answer
        else:
          continue
      else:
        index[key] = len(index)+1
        key_ = ''.join(msg[:j-1])
        answer.append(index[key_])
        del msg[:j-1]
        berak
  
  
  return answer
    
