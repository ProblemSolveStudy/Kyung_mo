# 1. 현재 큐의 가장 앞에 있는 문서의 '중요도'를 확인한다.
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 큐의 맨 뒤로 배치한다.

# 입력
# 첫번째 줄 : 전체 테스트케이스의 수

# 첫번째 테스트케이스 : 문서의 개수N과 현재 큐에서 몇번째인지
# 두번째 테스트케이스 : N개 문서의 중요도가 주어짐

# import sys
# t = int(sys.stdin.readline())

# for i in range(t):
#     n, m = map(int, sys.stdin.readline().rstrip().split())
#     imp = list(map(int, sys.stdin.readline().rstrip().split()))
#     idx = [0 for i in range(n)]
#     idx[m] = 1
#     cnt = 0

#     while True:
#         if imp[0] == max(imp):
#             cnt+=1
#             if idx[0] == 1:
#                 print(cnt)
#                 break
#             else:
#                 del imp[0]
#                 del idx[0]
#         else:
#             imp.append(imp[0])
#             del imp[0]
#             idx.append(idx[0])
#             del idx[0]

import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    imp = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    idx = deque([0 for i in range(n)])
    idx[m] = 1
    cnt = 0

    while True:
        if imp[0] == max(imp):
            cnt+=1
            if idx[0] == 1:
                print(cnt)
                break
            else:
                imp.popleft()
                idx.popleft()
        else:
            imp.append(imp.popleft())
            idx.append(idx.popleft())