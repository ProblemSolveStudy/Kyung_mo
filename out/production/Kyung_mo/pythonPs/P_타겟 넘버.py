def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        temp = []
        
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
        leaves = temp
    
    for i in leaves:
        if i == target:
            answer += 1
    
    return answer

print(solution([1,1,1,1,1], 3))