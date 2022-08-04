def solution(n):
  answer = []
  snail = [[0 for _ in range(i)] for i in range(n)]
  move = [[1,0], [0,1], [-1,-1]]   #DOWN, RIGHT, UP
  x, y = -1, 0
  num = 1
  
  dir = 0
  while dir < n:
    for _ in range(dir, n):
      if dir%3 == 0:
        nx = x + direct[0][0]
        ny = y + direct[0][1]
      elif dir%3 == 1:
        nx = x + direct[1][0]
        ny = y + direct[1][1]
      elif dir%3 == 2:
        nx = x + direct[2][0]
        ny = y + direct[2][1]
      snail[nx][ny] = num
      x, y = nx, ny
      num += 1
    dir += 1
  
  for row in snail:
    for num in row:
      answer.append(num)
  
  return answer
