def func(number, base):
    result = ''
    r_alpha = ['A','B','C','D','E','F']
    while number > 0:
        if number%base >= 10:
            r = r_alpha[number%base-10]
        else:
            r = str(number%base)
        result = r+result
        number = number//base
    return result

def solution(n, t, m, p):
    answer = ''
    number = ['0'] 
    for num in range(t*m):
        number.extend(func(num, n))
        if len(number) > t*m:
            break
    for i in range(p-1, t*m, m):  
        answer += number[i]
    return answer
