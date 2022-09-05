from collections import defaultdict
import math
def calc_time(in_time, out_time):
    in_h, in_m = in_time.split(':')
    out_h, out_m = out_time.split(':')
    return (int(out_h)*60+int(out_m)) - (int(in_h)*60+int(in_m))

def solution(fees, records):
    answer = []
    info = defaultdict(list)
    for record in records:
        time, num, io = record.split()
        info[num].append([time])  #{차번호:[입차시간, 출차시간, 입차시간..]}
    
    for num, num_info in info.items():
        if len(num_info)%2 == 1: #마지막 출차정보 없으면 [23:59] 출차정보 append
            num_info.append(['23:59'])
        time = 0
        for idx in range(0, len(num_info), 2):
            in_info, out_info = num_info[idx], num_info[idx+1]
            print(in_info, out_info)
            time += calc_time(in_info[0], out_info[0])
        if time <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3]
        answer.append([fee,num])
    answer.sort(key=lambda x:x[1])
    return [ans[0] for ans in answer]
