def solution(a, b, n):
    answer = 0
    while True:
        if n // a == 0:
            break
        remainder = n % a
        n = (n//a) * b
        answer += n
        n += remainder

    return answer