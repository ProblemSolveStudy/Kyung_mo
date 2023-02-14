# 내풀이
# 예제에서 가장 큰수로 나열하길래 그렇게 풀었음;;;;;;
# 이게 도대체 왜 그리디인가 생각해보면서 풀었음;;;;;

# import sys

# n = list(sys.stdin.readline().rstrip())

# n.sort(reverse=True)

# number = int(''.join(n))
    
# if number % 30 == 0:
#     print(number)
# else:
#     print(-1)

# 다른사람 풀이
# 해당 수가 3의 배수임을 알기 위한 공식이 필요함
# 해당 수가 3의 배수임을 알기위해서는 각 자리의 수의 합이 3이 되어야 함

# 이사람 풀이가 나보다 시간이 3배가 빠름;;;;;;

import sys

n = list(sys.stdin.readline().rstrip())

n.sort(reverse=True)

sum=0
for i in n:
    sum += int(i)

if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))