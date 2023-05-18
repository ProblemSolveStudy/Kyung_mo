def solution(n, m, section):
    answer = 0
    
    arr = [1] * (n+1)
    
    for i in section:
        arr[i] = 0
    cnt = 0
    
    for i in range(1, len(arr)):
        if arr[i] == 0:
            start = i
            end = start + m - 1
            if end > len(arr) - 1:
                start = len(arr) - m
                end = start + m - 1
            for i in range(start, end+1):
                arr[i] = 1
            cnt += 1
        else:
            continue
    return cnt

n=16
m=4
section = [2,3,15,16]

print(solution(n,m,section))