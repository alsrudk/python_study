# https://school.programmers.co.kr/learn/courses/30/lessons/12953#

from math import gcd

def get_lcm(a, b):
    return a*b // gcd(a,b)

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = get_lcm(lcm, arr[i])
    
    return lcm
