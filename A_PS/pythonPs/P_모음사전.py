# from itertools import product
# def solution(word):
#     char = ['A', 'E', 'I', 'O', 'U']
#     tmp = []
#     for i in range(1, 6):
#         for j in product(char, repeat=i):
#             tmp.append(''.join(list(j)))
#     tmp.sort()
    
#     return tmp.index(word)+1

# print(solution("AAAAE"))

from itertools import product

# 두 개의 iterable에서 Cartesian product을 생성
iterable1 = ['A', 'B']
iterable2 = [1, 2]
result = list(product(iterable1, repeat=3))
print(result)
