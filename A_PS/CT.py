import heapq
n,k,enemy = 2,	4	,[3, 3, 3, 3]
def solution(n, k, enemy):
    h = enemy[:k]
    for i in range(k, len(enemy)):
        n -= heapq.heappushpop(h, enemy[i])
        if n < 0:
            return i

solution(n,k,enemy)