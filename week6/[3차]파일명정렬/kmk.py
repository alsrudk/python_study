def split(file):
    head, number, tail = '','',''
    idx = 0
    while idx < len(file):
        if not file[idx].isdigit():
            head += file[idx]
            idx += 1
        else:
            break
    file = file[idx:]
    idx = 0
    while idx < len(file):
        if file[idx].isdigit():
            number += file[idx]
            idx += 1
        else:
            tail += file[idx:]
            break
    return head, number, tail

def solution(files):
    answer = []
    for idx, file in enumerate(files):
        head, number, tail = split(file)
        answer.append([head, number, tail, idx])
    
    answer.sort(key=lambda x:(x[0].lower(), (int(x[1])), x[3]))
    answer = [''.join(ans[:3]) for ans in answer]
    return answer
