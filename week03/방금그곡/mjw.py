# https://school.programmers.co.kr/learn/courses/30/lessons/17683

from math import ceil

def trans_code(music):
    for x in 'ACDFG':
        music = music.replace(x+'#', x.lower())
    return music

def get_playtime(st, end):
    start = int(st[:2])*60 + int(st[3:])
    end   = int(end[:2])*60 + int(end[3:])
    return end - start

def solution(m, musicinfos):
    m = trans_code(m)               # CC#BCC#BCC#BCC#B -> CcBCcBCcBCcB
    ans = []
    for m_info in musicinfos:
        st, end, m_name, code = m_info.split(',')
        code = trans_code(code)     # 'CC#B' -> CcBC
        playtime = get_playtime(st, end)
        repeatN = ceil(playtime/len(code))

        # CDEFGAB, 14 -> CDEFGABCDEFGAB  // ABCDEF, 5 -> ABCDE
        code = code * repeatN if len(code) < playtime else code[:playtime]
        
        if m in code:
            ans.append((m_name, playtime))
    
    if not ans:
        return '(None)'
    elif len(ans) > 1:
        ans.sort(key=lambda x: -x[1])
    return ans[0][0]
