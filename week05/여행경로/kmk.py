from collections import defaultdict
def solution(tickets):
    answer = []
    route = defaultdict(list)
    for ticket in tickets:
        route[ticket[0]].append(ticket[1])  
    for dep in route:                       #뒤에서부터 pop(), 역순으로 정렬
        route[dep].sort(reverse=True)
    
    stack = []
    stack.append('ICN')
    while stack:
        dep = stack[-1]  
        #아직 항공권 남아있음
        if dep in route and route[dep]: 
            next_dep = route[dep].pop()
            stack.append(next_dep)     nd
        #항공권 다 씀   
        else:                           
            answer.append(stack.pop())
            
    return answer[::-1] 
