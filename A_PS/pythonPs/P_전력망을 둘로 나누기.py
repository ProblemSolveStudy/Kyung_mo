from collections import deque
def solution(n, wires):
    answer = -1
    res = 0
    graph = [[] for _ in range(n+1)]
    
    def bfs(start):
        visited = [False] * (n+1)
        visited[start] = True
        cnt = 1
        q = deque([start])
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    cnt += 1
        return cnt
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    res = n
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        res = min(abs(bfs(a) - bfs(b)), res)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return res