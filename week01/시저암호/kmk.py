#!/usr/bin/env python
# coding: utf-8

# In[1]:


def solution(s, n):
    answer = ''
    for letter in s:
        if letter.isalpha(): #알파벳
            num = ord(letter)+n
            if letter.isupper() and num > 90:  #대문자이며 Z 넘어감
                ans = chr(num-90+64)
                answer += ans
            elif letter.islower() and num > 122:  #소문자이며 z 넘어감
                ans = chr(num-122+96)
                answer += ans
            else:  #범위 안
                answer += chr(num)
        else:   #공백
            answer += letter

    return answer

