# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    dest_len = len(number)-k                # 목표로 하는 문자열 길이 
    ans = ''
    while len(ans) < dest_len:              
        max_i = 0                           # 범위 내에서 가장 큰 숫자의 위치 탐색
        for i in range(len(number[:k+1])):  
            if number[i] == '9':
                max_i = i
                break
            if number[i] > number[max_i]:
                max_i = i
        
        ans += number[max_i]                # 그 숫자 추가
        number = number[max_i+1:]           # 탐색 범위 update
        k -= (max_i)                        # 제거할 숫자 개수 update
    return ans
