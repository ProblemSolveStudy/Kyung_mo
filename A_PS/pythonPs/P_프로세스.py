from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque((i,j) for i,j in enumerate(priorities))
    
    while True:
        temp = q.popleft()
        if any(temp[1] < k[1] for k in q):
            q.append(temp)
        else:
            answer += 1
            if temp[0] == location:
                return answer