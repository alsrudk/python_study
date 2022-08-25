from collections import defaultdict
def divide(file):
    file = file.lower()
    head, num, tail = '', '', ''
    idx = 0
    while idx<len(file):
        if not file[idx].isdigit():
            head+=file[idx]
            idx+=1
        else:
            break
    while idx<len(file):
        if file[idx].isdigit() and len(num)<6:
            num+=file[idx]
            idx+=1
        else:
            break
    tail += file[idx:]
    return head, int(num), tail

def solution(files):
    answer = []
    dic = defaultdict(list)
    for i,file in enumerate(files):
        dic[i].extend(divide(file))
    sort_lst = sorted(dic.items(), key= lambda value:(value[1][0], value[1][1]))
    
    for i in sort_lst:
        answer.append(files[i[0]])
    return answer
