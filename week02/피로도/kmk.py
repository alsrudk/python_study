from itertools import permutations
def solution(k, dungeons):
    index_list = list(range(len(dungeons)))                    #dungeons 인덱스 리스트
    candidates = list(permutations(index_list, len(dungeons))) #순열함수 - 모든 경우 탐색
    result = []
    
    #순서대로 돌기
    for candidate in candidates:      
        count = 0              #탐험한 dungeon 개수
        left = k               #남은 피로도
        for i in candidate:          
            if left >= dungeons[i][0]:      #남아있는 피로도가 최소 필요 피로도보다 크다면
                left -= dungeons[i][1]       
                count += 1
        result.append(count)  #각 경우마다 탐험한 dungeons 개수
        
    return max(result)         #탐험한 최대 dungeons 개수
