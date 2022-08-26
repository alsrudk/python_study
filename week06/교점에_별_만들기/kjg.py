from collections import deque
def point(line):
    que = deque(line)
    x = []
    y = []
    l = que.popleft()
    while que:
        try:
            for li in que:
                x.append((l[1]*li[2]-l[2]*li[1])/(l[0]*li[1]-l[1]*li[0]))
                y.append((l[2]*li[0]-l[0]*li[2])/(l[0]*li[1]-l[1]*li[0]))
        except:
            pass
        if que:
            l = que.popleft()
    return zip(x,y)

def solution(line):
    answer = []
    int_p = []
    for p in point(line):
        if p[0] == int(p[0]) and p[1] == int(p[1]):
            int_p.append((int(p[0]),int(p[1])))
    
    int_p = list(set(int_p))
    min_x, max_x = min(int_p, key=lambda p: p[0])[0], max(int_p, key=lambda p: p[0])[0]
    min_y, max_y = min(int_p, key=lambda p: p[1])[1], max(int_p, key=lambda p: p[1])[1]
    answer = [['.']*(max_x-min_x+1) for i in range(max_y-min_y+1)]
    for (x,y) in int_p:
        x -= min_x
        y -= min_y
        answer[y][x] = '*'
        
    return [''.join(k) for k in answer][::-1]
