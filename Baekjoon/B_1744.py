# 곱셈 : [음, 음], [양, 양], [음, 0]
# 묶은 수는 서로 곱한 후 더한다.
import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]

positive = []
negative = []

answer = 0

for i in num:
    if i > 1:
        positive.append(i)
    elif i <= 0:
        negative.append(i)
    else:
        answer += i

positive.sort(reverse=True)
negative.sort()

for i in range(0, len(positive), 2):
    if i+1 >= len(positive):
        answer += positive[i]
    else:
        answer += positive[i] * positive[i+1]

for i in range(0, len(negative), 2):
    if i+1 >= len(negative):
        answer += negative[i]
    else:
        answer += negative[i] * negative[i+1]

print(answer)
