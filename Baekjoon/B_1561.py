# n = 아이들 수 m = 놀이기구 수
# 3번 예제의 경우엔 8분에 모든 아이들이 탑승을 함
# 일단 모든 아이들이 탑승하는 시간을 구하기 위해서 이분탐색을 진행함
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))

if n<m:
    print(n)
else:
    start = 0
    end = max(arr) * n
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = m
        for i in arr:
            total += mid // i
        
        if total >= n:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    
    # 바로 직전시간까지 탑승한 아이들의 수
    cnt = m
    for i in range(m):
        cnt += (result-1) // arr[i]
    
    for i in range(m):
        if result % arr[i] == 0:
            cnt += 1
        if cnt == n:
            print(i+1)
            break