# mid = 평균적으로 아이들을 전부 태울 수 있는 시간대

# 예제 2번의 경우 6분에 교환됨
# 아이가 타게 되는 놀이기구의 번호를 알아내야 함

# 시간 T에 놀이기구 R에 탑승한 아이들의 수가 N일 때
# N = T/R이다?
import sys
input = sys.stdin.readline

#n 아이들 수 , m 놀이기구 개수
n,m = map(int, input().split())
time = list(map(int, input().split()))

if n < m:
    print(n)
else:
    start = 0
    end = 60000000000
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = m

        for t in time:
            total += mid // t
        
        if total >= n:
            result = mid
            end = mid - 1
        else:
            start = mid + 1


    cnt = m
    for i in range(m):
        cnt += (result - 1) // time[i]

    for i in range(m):
        if result % time[i] == 0:
            cnt += 1
        if cnt == n:
            print(i+1)
            break