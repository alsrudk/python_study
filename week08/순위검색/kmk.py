from collections import defaultdict
import bisect
def solution(info, query):
    answer = []
    data = defaultdict(list)
    for i in info:
        lan, dep, car,food, score = i.split()
        for lan_ in [lan, '-']:
            for dep_ in [dep, '-']:
                for car_ in [car, '-']:
                    for food_ in [food, '-']:
                        data[lan_,dep_,car_,food_].append(int(score))
    for score in data.values():
        score.sort()
        
    for q in query:
        cnt = 0
        q = q.split()
        lan, dep, car,food, score = q[0], q[2], q[4], q[6], int(q[7])
        score_list = data[lan,dep,car,food]
        cnt = bisect.bisect_left(score_list, score)
        answer.append(len(score_list)-cnt)
    return answer
