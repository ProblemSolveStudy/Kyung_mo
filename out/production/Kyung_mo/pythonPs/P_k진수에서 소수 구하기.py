def is_prime_num(k):
    if k == 2 or k == 3 : return True
    if k % 2 == 0 or k < 2 : return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ''
    while True:
        if n == 0:
            break
        temp = n % k
        n //= k
        num += str(temp)
    num = num[::-1]
    
    for n in num.split('0'):
        if n == '': continue
        if is_prime_num(int(n)):
            answer += 1
            
    return answer



print(solution(437674, 3))