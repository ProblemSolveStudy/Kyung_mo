import sys
from collections import deque
n = int(sys.stdin.readline())

deq = deque()

for i in range(n):
    com = sys.stdin.readline().rstrip().split()

    if com[0] == 'push_front':
        deq.append(com[1])

    elif com[0] == 'push_back':
        deq.appendleft(com[1])

    elif com[0] == 'pop_front':
        if deq: print(deq.pop())
        else: print(-1)

    elif com[0] == 'pop_back':
        if deq: print(deq.popleft())
        else: print(-1)

    elif com[0] == 'size':
        print(len(deq))

    elif com[0] == 'empty':
        if deq: print(0)
        else: print(1)

    elif com[0] == 'front':
        if not deq: print(-1)
        else: print(deq[-1])

    elif com[0] == 'back':
        if not deq: print(-1)
        else: print(deq[0])