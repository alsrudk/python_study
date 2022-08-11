# https://school.programmers.co.kr/learn/courses/30/lessons/17684

from collections import deque

def solution(msg):
    msgDict = {chr(x):i for i,x in enumerate(range(65,91),1)} # 90
    end_idx = 26
    maxlen = 1
    
    msg = deque(msg)
    answer = []
    while msg:
        cur = ''
        curlen = 0
        while msg and curlen < maxlen:
            cur += msg.popleft()
            curlen += 1
        
        while cur not in msgDict:
            msg.appendleft(cur[-1])
            cur = cur[:-1]
        answer.append(msgDict[cur])
        
        if msg:
            cur += msg.popleft()
            if cur not in msgDict:
                end_idx += 1
                msgDict[cur] = end_idx
                maxlen = max(len(cur), maxlen)
            msg.appendleft(cur[-1])
            cur = cur[:-1]

    return answer
