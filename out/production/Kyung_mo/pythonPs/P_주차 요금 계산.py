from math import ceil
def solution(fees, records):
    answer = []
    # 기본 시간 이하라면 기본 요금 청구
    # 기본 시간 초과 기본요금 + 단위요금
        # 단위 시간으로 나누어 떨어지지 않으면 (올림) 한다!
    # fee[0] 기본 시간, fee[1] 기본 요금 fee[2] 단위 시간 fee[3] 단위 요금
    
    parking_set = {}
    using_time = {}
    
    # 1.우선 시간을 전부 분으로 바꿔야 한다.
    for record in records:
        time, number, io = record.split()
        h,m = map(int, time.split(":"))
        time = h * 60 + m
        
        if io == 'IN':
            parking_set[number] = time
        elif io == 'OUT':
            if number in using_time:
                using_time[number] += time - parking_set[number]
            else:
                using_time[number] = time - parking_set[number]
            del parking_set[number]
    for number,time in parking_set.items():
        if number in using_time:
            using_time[number] += 1439 - time
        else:
            using_time[number] = 1439 - time
    
    for number,time in sorted(using_time.items(), key = lambda x:x[0]):
        answer.append(fees[1] + max(0, ceil((time - fees[0]) / fees[2])) * fees[3])
    
        
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])