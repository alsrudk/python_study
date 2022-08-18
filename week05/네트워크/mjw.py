from collections import defaultdict
from copy import deepcopy

def dfs(cur, n_tickets, ticketDict, route, best_route=[]):
    if len(route) == n_tickets+1:
        return route
    
    for nxt in ticketDict[cur]:
        tDict = deepcopy(ticketDict)
        tDict[cur].remove(nxt)
        new_route = dfs(nxt, n_tickets, tDict, route+[nxt], best_route)
        best_route = sorted([new_route, best_route])[0] if best_route else new_route
    return best_route

def solution(tickets):
    ticketDict = defaultdict(list)          # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    for (source, dest) in tickets:
        ticketDict[source].append(dest)
    n_tickets = len(tickets)
    return dfs('ICN', n_tickets, ticketDict, route=['ICN'])
