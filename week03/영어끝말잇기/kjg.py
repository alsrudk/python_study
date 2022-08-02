def solution(n, words):
    answer = []
    # 끝말이 안이어질때
    # 겹치는 단어가 있을때
    # 순서
    i_lst = [0 for _ in range(n)]
    check = set()
    last_word = words[0][0]
    for i,w in enumerate(words):
        if w not in check and last_word == w[0]:
            i_lst[i%n] += 1
            check.add(w)
            last_word = w[-1]
        else:
            answer.append((i%n)+1)
            answer.append(i_lst[i%n]+1)
            break
    if answer == []:
        answer = [0,0]  
    
    return answer
