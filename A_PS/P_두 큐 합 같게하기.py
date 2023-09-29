from collections import deque
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    answer = -2
    s1, s2 = sum(queue1), sum(queue2)
    cnt = 0
    
    if s1 == s2:
        return 0
    if (s1+ s2) % 2 == 1:
        return -1
    
    while True:
        if s1 > s2:
            i = queue1.popleft()
            queue2.append(i)
            s1 -= i
            s2 += i
            cnt += 1
        elif s2 > s1:
            i = queue2.popleft()
            queue1.append(i)
            s2 -= i
            s1 += i
            cnt += 1
        else:
            break
        
        if cnt == 300000:
            return -1
    return cnt