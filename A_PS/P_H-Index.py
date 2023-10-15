def solution(citations):
    answer = 0
    # 지표를 구하고자 한다
    # h의 최대값을 구하겠다
    # len(citations) -> 발표한 논문 수
    # 그 중 3편의 논문이 3회 이상 인용됐어 (binary search?)
    # 나머지는 3회 이하 인용됐기에 최대 인용 횟수가 3회이다?
    
    # 이분탐색까지 해야하나? 시간복잡도? 1000편? 백만
    
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