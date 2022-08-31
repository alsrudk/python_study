from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    
    while answer < (len(queue1)+len(queue2))*2:
        if sum_queue1 == sum_queue2:
            return answer
            break
        if sum_queue1 < sum_queue2 and queue2:
            i = queue2.popleft()
            queue1.append(i)
            sum_queue2 -= i
            sum_queue1 += i
            answer += 1
        elif sum_queue1 > sum_queue2 and queue1:
            i = queue1.popleft()
            queue2.append(i)
            sum_queue1 -= i
            sum_queue2 += i
            answer += 1
            
    
    return -1
