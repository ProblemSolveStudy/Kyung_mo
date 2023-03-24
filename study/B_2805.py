# python3으로 제출했을 때 시간초과가 났음
# pypy3으로 제출했을 댄 시간초과가 나지 않음
# 그 이유로는 pypy3의 경우 자주쓰이는 코드 (해당 코드에서는 while의 1억,2억번 반복)
# 에 대해서 캐싱하는 기능이 있기 때문에 pypy에서는 통과했음

# 추가로 파이썬은 문제에 명시된 시간보다 *3+2의 시간제한을 더 받게 된다. 즉 해당문제에서는
# 5초의 시간을 받게 되는건데, 그래서 마지막 제출인 5000ms가 통과했나보다 ㅎ
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)