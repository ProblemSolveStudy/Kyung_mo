# 만들어질 수 있는 가장 큰 수를 구하는 프로그램
# 각 숫자 사이에 x 혹은 +연산자를 넣어야 함

# 문제풀이 과정
# 곱하는 것이 많아질 수록 가장 큰 수가 될 것이야

#내풀이

import time
start = time.time()




import sys
S = list(map(int, sys.stdin.readline().rstrip()))
result = 0

for i in S:
    if i <= 1 or lastnumber <=1:
        result += i
    else:
        result *= i
    lastnumber = i

print(result)

# 답지 풀이

# data = input()

# result = int(data[0])

# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)

print("time :", time.time() - start)