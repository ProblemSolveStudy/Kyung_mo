# 시간초과때문에 반복문은 최대한 1번으로 끝내야만 한다.
# 내 코드의 시간복잡도는 O(nlogn)

import sys

n,L = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
arr.sort()
cnt = 0
plank=0
for start, end in arr:
    poolLength = end - start
    
    if plank > start:
        poolLength -= plank - start
        start = plank
        
    if poolLength % L == 0:
        cnt += poolLength // L
        plank = poolLength
    else:
        cnt += poolLength // L + 1
        plank = end + L - (poolLength % L)

print(cnt)
    

# plank = 0
# cnt = 0
# for start, end in arr:
#     if plank > start:
#         start = plank
#     while start < end:
#         start += L
#         cnt += 1

#     plank = start

# print(cnt)