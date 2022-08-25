# https://school.programmers.co.kr/learn/courses/30/lessons/87377

from itertools import combinations

def solve(l1, l2):
    (a, b, e), (c, d, f) = l1, l2
    flag, (x,y) = False, (0, 0)
    if a*d - b*c != 0:
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
        flag = True
    return flag, (x, y)
    
def solution(line):
    points = set()
    for (i,j) in combinations(range(len(line)), 2):
        flag, (x,y) = solve(line[i], line[j])
        if flag and int(x)==x and int(y)==y:
            points.add((int(x),int(y)))
    
    min_x, max_x = min(points, key=lambda p: p[0])[0], max(points, key=lambda p: p[0])[0]
    min_y, max_y = min(points, key=lambda p: p[1])[1], max(points, key=lambda p: p[1])[1]
    
    answer = [['.']*(max_x-min_x+1) for _ in range(max_y-min_y+1)]
    for (x,y) in points:
        x += (-1)*min_x
        y += (-1)*min_y
        answer[y][x] = '*'
        
    return [''.join(k) for k in answer][::-1]
