def solution(n, left, right):
    answer = []
    # 몫과 나머지 중 max값을 선택후 + 1
    for i in range(left,right+1):
        a = i // n
        b = i % n
        answer.append(max(a,b) + 1)
    
    
    return answer

print(solution(3, 2, 5))