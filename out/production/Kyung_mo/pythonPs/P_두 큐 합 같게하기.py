from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    cnt = 0
    
    if (s1+s2) % 2 == 1:
        return -1        

    
    while True:
        if s1 == s2:
            return cnt
        if s1>s2:
            temp = q1.popleft()
            q2.append(temp)
            s1 -= temp
            s2 += temp
            cnt += 1
        elif s1<s2:
            temp = q2.popleft()
            q1.append(temp)
            s1 += temp
            s2 -= temp
            cnt += 1
        else:
            break
    
        if cnt > 300000:
            return -1
    return cnt