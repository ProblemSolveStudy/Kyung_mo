def solution(progresses, speeds):
    answer = []
    dayCnt = 0
    cnt = 0
    while progresses:
        if progresses[0] + dayCnt * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            dayCnt += 1
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
    answer.append(cnt)
        
    return answer