import sys
from collections import deque

# 값을 뽑아내는 것은 popleft()밖에 없음

n,m = map(int,sys.stdin.readline().split())
command = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1, n+1)])

cnt = 0

for i in command:
    while True:
        if deq[0] == i:
            deq.popleft()
            break
        else:
            if deq.index(i) <= len(deq)//2:
                deq.rotate(-1)
                cnt += 1
            else:
                deq.rotate(1)
                cnt += 1

print(cnt)