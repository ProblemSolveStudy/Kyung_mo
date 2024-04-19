def solution(k, dungeons):
    global answer
    answer = 0
    visited = [False] * len(dungeons)
    def dfs(k, dungeons, cnt):
        global answer
        if cnt > answer:
            answer = cnt
        
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= k:
                visited[i] = True
                dfs(k-dungeons[i][1], dungeons, cnt + 1)
                visited[i] = False
    
    dfs(k, dungeons, 0)
        
    return answer