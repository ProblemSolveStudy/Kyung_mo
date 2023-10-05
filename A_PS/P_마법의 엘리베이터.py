from collections import deque
# 0층으로 가야 한다.
def solution(storey):
    answer = 0
    max = 100_000_000
    
    visited = [0] * (max+1)
    
    def bfs(start):
        q = deque([start])
        while q:
            s = q.popleft()
            
            if s == 0:
                return visited[s]
            
            for ns in (s + 1, s - 1, s + 10, s - 10):
                if 0<ns<=max and not visited[ns]:
                    visited[ns] = visited[s] + 1
                    q.append(ns)
                
    answer = bfs(storey)
    
    return answer

print(solution(16))