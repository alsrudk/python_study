def solution(survey, choices):
  answer = ''
  score = {1: 3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
  result = {'R':0 ,'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
  
  for i in range(len(survey)):
    if choices[i] == 4:
      result[survey[i][0]] += 0
      result[survey[i][1]] += 0
    elif choices[i] > 4:
      result[survey[i][1]] += score[choices[i]]
    elif choices[i] < 4:
      result[survey[i][0]] += score[choices[i]]
    
  if result['R'] > result['T']:
    answer += 'R'
  elif result['R'] < result['T']:
    answer += 'T'
  else:
    answer += 'R'

  if result['C'] > result['F']:
    answer += 'C'
  elif result['C'] < result['F']:
    answer += 'F'
  else:
    answer += 'C'

  if result['J'] > result['M']:
    answer += 'J'
  elif result['J'] < result['M']:
    answer += 'M'
  else:
    answer += 'J'

  if result['A'] > result['N']:
    answer += 'A'
  elif result['A'] < result['N']:
    answer += 'N'
  else:
    answer += 'A'
  
  
  return answer
