def checkLine(place):
    for r in range(len(place)):
        for c in range(len(place)):
            if place[r][c] == 'P':
                if c < len(place)-1 and place[r][c+1] == 'P':
                    return False
                elif c < len(place) -2 and place[r][c+1] == 'O' and place[r][c+2] == 'P':
                    return False
    place = [list(reversed(i)) for i in zip(*place)]
    for r in range(len(place)):
        for c in range(len(place)):
            if place[r][c] == 'P':
                if c < len(place)-1 and place[r][c+1] == 'P':
                    return False
                elif c < len(place) -2 and place[r][c+1] == 'O' and place[r][c+2] == 'P':
                    return False
    return True

def checkCross(place):
    for r in range(len(place)-1):          
        for c in range(len(place)-1):     
            if place[r][c] == 'P' and place[r+1][c+1] == 'P':
                if place[r+1][c] == 'O' or place[r][c+1] == 'O':
                    return False
    for r in range(len(place)-1):          
        for c in range(1,len(place)):      
            if place[r][c] == 'P' and place[r+1][c-1] == 'P':
                if place[r][c-1] == 'O' or place[r+1][c] == 'O':
                    return False
    return True

def solution(places):
    answer = []

    for place in places:
        for i in range(len(place)):
            place[i] = list(place[i])
        if checkLine(place) and checkCross(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
