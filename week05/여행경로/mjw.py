# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict
from copy import deepcopy

def dfs(cur, n_tickets, ticketDict, root, best_root=[]):
    if len(root) == n_tickets+1:
        return root
    
    for nxt in ticketDict[cur]:
        tDict = deepcopy(ticketDict)
        tDict[cur].remove(nxt)
        new_root = dfs(nxt, n_tickets, tDict, root+[nxt], best_root)
        best_root = sorted([new_root, best_root])[0] if best_root else new_root
    return best_root

def solution(tickets):
    ticketDict = defaultdict(list)          # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    for (source, dest) in tickets:
        ticketDict[source].append(dest)
    n_tickets = len(tickets)
    return dfs('ICN', n_tickets, ticketDict, root=['ICN'])
