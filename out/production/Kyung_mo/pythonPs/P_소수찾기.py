from itertools import permutations
def solution(numbers):
    answer = 0
    nums = []
    for i in range(1, len(numbers) + 1):
        nums.append(list(map(''.join , permutations(numbers, i))))
    nums = set(map(int, sum(nums, [])))
    
    for n in nums:
        if is_prime(int(n)): answer += 1
    
    return answer

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True