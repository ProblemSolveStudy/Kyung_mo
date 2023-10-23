import math
answer = 0
k=2
d=4

for i in range(0, d+1, k):
    res = math.floor(math.sqrt(d*d - i*i))
    answer += (res // k) + 1

print(math.sqrt(12))