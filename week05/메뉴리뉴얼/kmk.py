from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        menu = []
        for order in orders:
            order = sorted(list(order))
            candidates = list(combinations(order, c))
            menu.extend([''.join(candidate) for candidate in candidates]) #주문한 단품메뉴 중 가능한 조합들
            
        count = dict() #가능한 조합들 개수 카운트
        for m in menu:
            try:
                count[m] += 1
            except:
                count[m] = 1
                
        max_count = max(count.values())  #가장 많이 함께 주문된 단품메뉴 조합
        if max_count >= 2:               #최소 2명 이상의 손님이 주문
            pick = [key for key, value in count.items() if value == max_count]
            answer.extend(pick)
    
    return sorted(answer)
