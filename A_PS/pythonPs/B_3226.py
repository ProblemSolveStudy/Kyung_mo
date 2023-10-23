import sys
time = []
answer = 0
for i in range(int(sys.stdin.readline())):
    time.append(list(sys.stdin.readline().split()))
    h,m = map(int,time[i][0].split(":"))
    start = h*60 + m # 시작시간
    spend = int(time[i][1])
    end = (start+spend)

    if 420 <= start < 1140 and 420 <= end < 1140:
        answer += spend * 10
    elif (start < 420 or start >= 1140) and (end <= 420 or end >= 1140):
        answer += spend * 5
    else:
        if start <= 420 and end > 420:
            prev = 420 - start
            answer += prev * 5
            next = end - 420
            answer += next * 10

        if start < 1140 and (end >= 1140 or end < 420):
            prev = 1140 - start
            answer += prev * 10
            next = min(end - 1140, end - 420)
            answer += next * 5
print(answer)