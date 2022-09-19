# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c]=='P':
                if c < 4 and place[r][c+1]=='P':
                    return 0
                if r < 4 and place[r+1][c]=='P':
                    return 0
                if c < 3 and place[r][c+1]=='O' and place[r][c+2]=='P':
                    return 0
                if r < 3 and place[r+1][c]=='O' and place[r+2][c]=='P':
                    return 0
                if r<4 and c<4 and (place[r][c+1]=='O' or place[r+1][c]=='O') and place[r+1][c+1]=='P':
                    return 0
                if r>0 and c<4 and (place[r][c+1]=='O' or place[r-1][c]=='O') and place[r-1][c+1]=='P':
                    return 0
    return 1
    
def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer
