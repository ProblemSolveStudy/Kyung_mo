# def recursive_funtion(i):
#     if i==100:
#         return
#     print(i, "번째 재귀함수를 호출합니다")
#     recursive_funtion(i+1)
#     print(i, "번째 재귀함수를 종료합니다.")

# recursive_funtion(1)

# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# def factorial_recursive(n):
#     if n<= 1:
#         return 1
#     return n*factorial_recursive(n-1)

# print(factorial_recursive(5))

# 유클리드 호제법
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

print(gcd(50, 30))