import heapq
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    h=[]
    
    for i in range(len(enemy)):
        heapq.heappush(h, enemy[i])
        
        if len(h) > k:
            last = heapq.heappop(h)
            if last > n:
                return i
            n -= last
    return len(enemy)