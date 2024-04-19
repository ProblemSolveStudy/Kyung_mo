def solution(numbers):
    answer = ''
    nums = []
    # permutations는 시간초과 O(n!)
    
    nums = list(map(str, numbers))
    nums.sort(key = lambda x : x*3, reverse=True)
    
    for i in nums:
        answer += i
        
    return str(int(answer))