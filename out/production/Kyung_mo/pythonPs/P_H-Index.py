def solution(citations):
    answer = 0 
    citations = sorted(citations, reverse=True)
    start = 0
    end = len(citations) - 1
    
    while start<=end:
        mid = (start + end) // 2
        
        if citations[mid] >= mid + 1:
            answer = mid + 1
            start = mid + 1
        else:
            end = mid - 1
    return answer

print(solution([6,4,3,1,0]))