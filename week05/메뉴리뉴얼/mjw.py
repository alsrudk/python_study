# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from collections import Counter, defaultdict
from itertools import combinations

def solution(orders, course):
    orderDict = {c: Counter() for c in course}
    for odr in orders:
        for c in course:
            if c <= len(odr):
                orderDict[c].update([''.join(sorted(x)) for x in combinations(list(odr), c)])
    
    ans = []
    for c in course:
        if orderDict[c]:
            sorted_sets = orderDict[c].most_common()
            maxi = sorted_sets[0][1]
            for sets, odrN in sorted_sets:
                if maxi >= 2 and odrN == maxi:
                    ans.append(sets)
    return sorted(ans)
