def n_change(n,t,m):
    n_change = ''
    dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    for i in range(t*m):
        if i == 0:
            n_change+=str(i)
        else:
            num = ''
            while i>0:
                if i%n > 9:
                    num+=dic[i%n]
                else:
                    num+=str(i%n)
                i //= n
            num = num[::-1]
            n_change+=num
    return n_change

def solution(n, t, m, p):
    answer = ''
    for n in n_change(n,t,m)[p-1:t*m:m]:
        answer+=n
    return answer
