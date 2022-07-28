def solution(number, k):
    answer = ''
    d = len(number)-k
    while len(answer) < d:
        max_i = 0
        for i in range(len(number[:k+1])):
            if number[i] == '9':
                max_i = i
                break
            else:
                if number[i] > number[max_i]:
                    max_i = i
        answer += number[max_i]
        number = number[max_i+1:]
        k -= max_i
        
    return answer
# 지원이꺼 참고
