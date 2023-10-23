import sys
n,m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2 # 커팅기
    for x in trees:
        if x > mid:
            total += x - mid
    
    if total < m: # 잘린게 필요한것 보다 적어! 그럼 더 많이 잘라야 하지
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)