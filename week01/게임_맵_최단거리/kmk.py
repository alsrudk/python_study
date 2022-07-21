#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
def solution(maps):
    queue = deque([])
    queue.append([0,0])  #시작지점
    
    n = len(maps)-1 #row-1
    m = len(maps[0])-1  #column-1
    
    dx = [-1,0,1,0] 
    dy = [0,-1,0,1]
     
    #방문 여부 기록해주기 위해 visited 생성, visited[x][y]에 들어있는 값은 (x,y)까지 오기위해 걸린 시간
    visited = [[0] * (m+1) for _ in range(n+1)] 
    visited[0][0] = 1 #시작 위치 방문
    
    while queue:
        x,y = queue.popleft()
        if x == n and y == m:  #(n,m)에 도달하면 종료
            return visited[x][y]
        for i in range(4):  #상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=n and 0<=ny<=m:  #map을 벗어나지 않고,
                if maps[nx][ny] == 1:  #벽이 아니며,
                    if visited[nx][ny] == 0:   #아직 방문한 길이 아닐 경우
                        visited[nx][ny] = visited[x][y] + 1 #여태까지 왔던 칸 길이 + 1
                        queue.append([nx,ny])
        
    return -1   #위에서 return되지 않았다면 (n,m)에 도달하지 못함 -1 return

