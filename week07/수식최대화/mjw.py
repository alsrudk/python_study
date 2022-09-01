# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations

def calc(a,b,op):
    if   op == '+': res = a + b
    elif op == '-': res = a - b
    else:           res = a * b
    return res

def calc_by_priority(priority, nums, operations):
    for op in priority:
        while op in operations:
            i = operations.index(op)
            a, b = nums[i], nums[i+1]
            n = calc(a,b,op)
            # update
            operations = operations[:i] + operations[i+1:]
            nums = nums[:i] + [n] + nums[i+2:]
    return nums[0]

def solution(expression):
    tmp = expression.replace('+',' ').replace('-',' ').replace('*',' ')
    nums = list(map(int, tmp.split()))
    operations = [x for x in expression if not x.isdigit()]
    
    maxi = 0
    used_op = set(operations)
    for priority in permutations(used_op, len(used_op)):
        res = calc_by_priority(priority, nums, operations)
        maxi = max(abs(res), maxi)
    return maxi
