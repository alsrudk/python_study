# https://school.programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    ans = []
    for n in numbers:
        bn = bin(n)[2:]
        
        if n % 2 == 0:
            res = bn[:-1] + '1'
        else:
            if '0' not in bn:
                bn = '0' + bn
            i = bn.rfind('01')
            res = bn[:i] + '10' + bn[i+2:]
            
        ans.append(int(res,2))
    return ans
