import copy
max_diff = 0
candidates = []

#낮은 점수를 더 많이 맞힌 경우 비교함수
def compare(origin, new):
  for idx in range(10, -1, -1):
    if origin[idx] > new[idx]:
      return False
    elif origin[idx] < new[idx]:
      return True

#점수차 계산
def checkScore(info, ryan_info):
  a_sc, r_sc = 0, 0
  for i in range(11):
    if info[i] == 0 and ryan_info[i] == 0:
      continue
    elif info[i] >= ryan_info[i]:
      a_sc += (10-i)
    else:
      r_sc += (10-i)
  return r_sc-a_sc


def dfs(n, score, info, ryan):
    global candidates, max_diff
    if n == 0 and score == 0:      #화살 다 썼거나, 0점까지 다 돈 경우
      if score == 0:               #만약 남아있는 화살이 있으면 0점에 더해주기
        ryan[10] = n              
      result = checkScore(info, ryan) #점수차 계산
      if result > 0:                  #ryan 점수가 더 크다면
        if max_diff < result:         #case1: max값 갱신
          candidates = copy.deepcopy(ryan)
          max_diff = result
        elif max_diff == result and compare(candidates, ryan): #case2: max값 같을 경우 더 낮은 점수를 많이 맞춘 경우로 갱신
          candidates = copy.deepcopy(ryan)
      return 
    
    idx = 10-score
    #ryan이 해당 점수 획득
    if n > info[idx]:
      ryan_ = copy.deepcopy(ryan)
      ryan_[idx] = info[idx]+1
      dfs(n-info[idx]-1, score-1, info, ryan_)
    #ryan이 해당 점수 포기
    ryan_ = copy.deepcopy(ryan)
    dfs(n, score-1, info, ryan_)
    
def solution(n, info):
  global candidates
  ryan = [0 for _ in range(11)]
  dfs(n, 10, info, ryan)
  return candidates if candidates else [-1]
          

          
    
