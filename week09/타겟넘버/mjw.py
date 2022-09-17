# https://school.programmers.co.kr/learn/courses/30/lessons/43165

from itertools import product

def solution(numbers, target):
    numbers = [(x, -x) for x in numbers]
    
    answer = 0
    for nums in product(*numbers):
        if sum(nums) == target:
            answer += 1
    return answer
