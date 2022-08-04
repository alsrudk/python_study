def find(m, n, board):
    result = 0
    found = set()
    for x in range(m-1):
        for y in range(n-1):
            if board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1]:
                if board[x][y] != 0:
                    found.add((x,y))
                    found.add((x+1,y))
                    found.add((x,y+1))
                    found.add((x+1,y+1))
    if not found:
        return 0
    else:
        for x, y in found:
            board[x][y] = 0
        result += len(found)
        return result
    
def move(m, board):
    board = [list(i) for i in zip(*board)]  #세로로 묶어서 list 만들기                         
    for row in board:
        for i in range(m):
            if row[i] == 0 and i != 0:      
                count = 1                   #0의 개수
                index = i                   #인덱스 저장
                while True:
                    index += 1
                    if index < m and row[index] == 0:   #범위 내에 있으며 row[index] == 0
                        count += 1
                    else:
                        break
                for j in range(i-1, -1, -1):     #0이 시작되는 위치 바로 앞부터 아래로 땡겨줌
                    row[j+count] = row[j]        #0개수만큼 땡기면 됨
                for j in range(count):           #다시 맨 위부터 0을 채워넣어줌
                    row[j] = 0
    board = [list(i) for i in zip(*board)]
    return board    

def solution(m, n, board):
    for i in range(len(board)):
        board[i] = list(board[i])
    answer = 0
    
    found = 0
    while True:
        found = find(m, n, board)
        if found != 0:
            answer += found
            board = move(m, board)
        else:
            break    
            
    return answer
  
  
  
  
'''
T T T A N T        T 0 0 T T T    
0 0 F A 0 0        T 0 0 0 T M
0 0 0 F 0 0  ->    T F 0 0 M M   
T 0 0 R A A        A A F R M T
T T M M M F        N 0 0 A M T
T M M T T J        T 0 0 A F J

 0  1  2  3  4  5 
[T, F, 0, 0, M, M]  
count = 1
index = i = 2    #0이 시작되는 위치

=>  i = 2, count = 2

for j in range(i-1, -1, -1):   (1, 0)
  row[j+count] = row[j]        row[1+2] = row[1]   [T, F, 0, _F, M, M]  
                               row[0+2] = row[0]   [T, F, _T, _F, M, M]  
for j in range(count):
  row[j] = 0                                       [0, 0, T, F, M, M]  
'''
