# 적절한 높이를 찾을 때 까지 이진 탐색을 수행해서 높이를 조정하면 된다?
# 조건의 만족 여부에 따라서 탐색 범위를 좁혀서 해결이 가능하다?
# 큰 탐색범위를 보게 되면 이진탐색을 무조건 생각하도록 하자

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result)