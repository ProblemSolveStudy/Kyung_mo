# import sys

# result = 0
# i=1
# while True:
#     l, p, v = map(int, sys.stdin.readline().split())
#     if l+p+v == 0:
#         break
#     result = (v // p) * l
#     result += min((v%p), l)
#     print("Case " + str(i) + ": " + str(result))
#     i+=1

import sys

result = 0
i = 1
while True:
    l, p ,v = map(int, sys.stdin.readline().split())

    if l + p + v == 0:
        break

    result = (v//p) * l
    result += min((v%p), l)
    print("Case %d: %d" %(i, result))
    i+=1