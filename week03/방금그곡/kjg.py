def rep(t):
    t = t.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return t

def solution(m, musicinfos):
    answer = ''
    m = rep(m)
    a_lst = []
    for music in musicinfos:
        st,end,title,melody = music.split(',')
        melody = rep(melody)
        time = (int(end[:2])*60+int(end[3:])) - (int(st[:2])*60+int(st[3:]))
        n = time/len(melody)
        melody = melody*int(n)+melody[:int((n-int(n))*len(melody))+1] if n > 1 else melody[:time+1]
        if m in melody:
            a_lst.append((title,time))
    
    if not a_lst:
        answer += '(None)'
    else:
        a_lst.sort(key=lambda x:-x[1])
        answer += a_lst[0][0]
    return answer
