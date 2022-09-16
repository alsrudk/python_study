def hanoi(n, hanoi_list, depart, other, arrival): 
    if n == 1:
        hanoi_list.append([depart, arrival])
    else:
        hanoi(n-1, hanoi_list, depart, arrival, other)
        hanoi(1, hanoi_list, depart, other, arrival)
        hanoi(n-1, hanoi_list, other, depart, arrival)
    return hanoi_list

def solution(n):
    return hanoi(n, [], 1, 2, 3)
