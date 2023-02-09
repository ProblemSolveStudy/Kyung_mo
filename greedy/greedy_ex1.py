# N이 1이 될 때 까지 두 과정 중 하나를 반복해야 한다.
# 1. N에서 1을 뺀다 뺀 값이 N이 되어야 함
# 2. N을 K로 나눈다. 나눴을때엔 몫을 가져와야 함
# 3. 최소한의 반복횟수를 구해야만 함 (나누기를 최대한 많이 해야한다)

import sys
n,k = map(int, sys.stdin.readline().split())

cnt =0

# 내 풀이

# while n!=1:
#     if n%k == 0:
#         n //= k
#         cnt+=1
#     else:
#         n-=1
#         cnt+=1

# print(cnt)



while True:
    target = (n // k) * k # N이 K로 나누어 떨어지는 수가 될 때 까지 빼기
    cnt += (n-target)
    n = target
    if n < k: #N이 K로 나누어 떨어지지 않는다면!
        break
    cnt += 1
    n //= k
    
cnt += n-1
print(cnt)
