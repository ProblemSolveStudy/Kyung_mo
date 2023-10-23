import heapq
book_time = [["00:01","00:10"],["00:19","00:29"]]
def solution(book_time):
    answer = 0
    result = []
    for i in range(len(book_time)):
        for j in range(len(book_time[i])):
            h,m = map(int, book_time[i][j].split(":"))
            st = h*60 + m
            book_time[i][j] = st
    
    book_time.sort()
    heapq.heappush(result, book_time[0][1])
    
    
    for i in range(1, len(book_time)):
        if result[0] + 10 > book_time[i][0]:
            heapq.heappush(result,book_time[i][1])
        else:
            heapq.heappop(result)
            heapq.heappush(result, book_time[i][1])
    answer = len(result)   
    return answer

print(solution(book_time))