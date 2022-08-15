def solution(n, a, b):
  answer = 0
  players = [(i+1) for i in range(n)]

  while True:
    answer += 1
    game = []
    for i in range(0,len(players),2):
      match = players[i:i+2]
      game.append(match)

    for g in game:
      if [a,b] in game:
        return answer
    
    players = [(i+1) for i in range(len(players)//2)]

    if a%2 == 0:
      a = a//2
    else:
      a = a//2+1
      
    if b%2 == 0:
      b = b//2
    else:
      b = b//2+1
