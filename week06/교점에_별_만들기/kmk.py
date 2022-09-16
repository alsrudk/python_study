def calc(line):
  inter = set()
  for i in range(len(line)):
    for j in range(len(line)):
      if j == i:
        break
      if (line[i][0]*line[j][1]-line[i][1]*line[j][0]) != 0:
        x = (line[i][1]*line[j][2]-line[i][2]*line[j][1])/(line[i][0]*line[j][1]-line[i][1]*line[j][0])
        y = (line[i][2]*line[j][0]-line[i][0]*line[j][2])/(line[i][0]*line[j][1]-line[i][1]*line[j][0])
        if int(x) == x and int(y) == y:
          inter.add((int(x),int(y)))
  return inter

def solution(line):
  answer = []
  inter = calc(line)
  min_x, min_y = min([i[0] for i in inter]), min([i[1] for i in inter])
  max_x, max_y = max([i[0] for i in inter]), max([i[1] for i in inter])
  n, m = max_y-min_y, max_x-min_x
  
  answer = [['.' for _ in range(m+1)] for _ in range(n+1)]
  for (x,y) in inter:
    x -= min_x
    y -= min_y
    answer[y][x] = '*'
  return [''.join(k) for k in answer][::-1]
