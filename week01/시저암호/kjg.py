def solution(s, n):
    answer = ''
    l_lst = list(map(chr, range(97,123))) #ASCII 값
    u_lst = list(map(chr, range(65,91)))
    for a in s:
        if a in l_lst:
            if l_lst.index(a) + n < len(l_lst):
                answer += l_lst[l_lst.index(a)+n]
            else:
                answer += l_lst[l_lst.index(a)+n-len(l_lst)]
        elif a in u_lst:
            if u_lst.index(a) + n < len(u_lst):
                answer += u_lst[u_lst.index(a)+n]
            else:
                answer += u_lst[u_lst.index(a)+n-len(u_lst)]
        elif a == ' ':
            answer += ' '
    return answer
