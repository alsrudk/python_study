def solution(dirs):
    x,y = 0,0
    answer = dict()
    
    for dir in dirs:
        if dir == 'U' and y < 5: 
            answer[(x, y, x, y+1)] = True
            y += 1
        elif dir == 'D'and y > -5:
            answer[(x, y-1, x, y)] = True
            y -= 1
        elif dir == 'L' and x > -5:
            answer[(x-1, y, x, y)] = True
            x -= 1
        elif dir == 'R' and x < 5:
            answer[(x, y, x+1, y)] = True
            x += 1
    
    return len(answer)
