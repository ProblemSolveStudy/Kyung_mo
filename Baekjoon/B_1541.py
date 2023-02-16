import sys

# arr = sys.stdin.readline().split('-')
# num = []
# for i in arr:
#     sum = 0
#     s = i.split('+')
#     for j in s:
#         sum += int(j)
    
#     num.append(sum)

# n = num[0]
# for i in range(1, len(num)):
#     n -= num[i]

# print(n)

arr = sys.stdin.readline().split('-')
num = []
for i in arr:
    sum = 0
    s = i.split('+')
    for j in s:
        sum += int(j)
    num.append(sum)

n = num[0]
for i in range(1, len(num)):
    n -= num[i]

print(n)