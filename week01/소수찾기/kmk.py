#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
def solution(n):
    answer = []
    
    def check(number):
        for i in range(2, int(math.sqrt(number))+1):
            if number%i == 0:
                return False
        return True
    
    for j in range(2,n+1):
        if check(j):
            answer.append(j)
            
    return len(answer)

