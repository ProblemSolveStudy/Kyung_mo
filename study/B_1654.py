import sys
input = sys.stdin.readline
k,n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)
result = 0
while (start <= end):
    total = 0 # 랜선 수
    mid = (start+end) // 2 # 중앙값
    for x in arr: # x의 값을 확인해봄
        total += x // mid # 
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)