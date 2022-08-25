def solution(survey, choices):
    answer = ''
    cha_type = ['R','T','C','F','J','M','A','N']
    dic = {}
    for c in cha_type:
        dic[c] = 0
    
    for s,c in zip(survey,choices):
        if c>4:
            dic[s[1]] += c-4
        elif c<4:
            dic[s[0]] += 4-c
    if dic['R']>dic['T']:
        answer+='R'
    elif dic['R']<dic['T']:
        answer+='T'
    elif dic['R'] == dic['T']:
        answer+='R'
    if dic['C']>dic['F']:
        answer+='C'
    elif dic['C']<dic['F']:
        answer+='F'
    elif dic['C'] == dic['F']:
        answer+='C'
    if dic['J']>dic['M']:
        answer+='J'
    elif dic['J']<dic['M']:
        answer+='M'
    elif dic['J'] == dic['M']:
        answer+='J'
    if dic['A']>dic['N']:
        answer+='A'
    elif dic['A']<dic['N']:
        answer+='N'
    elif dic['A']==dic['N']:
        answer+='A'
    
    return answer
